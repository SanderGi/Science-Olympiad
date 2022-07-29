from cmath import inf
import RPi.GPIO as GPIO
import LCD_I2C
import NAU7802_I2C
import smbus2
import time

# Create the bus
bus = smbus2.SMBus(1)

# initialize the NAU7802 ADC
adc = NAU7802_I2C.NAU7802()
if adc.begin(bus):
    print("Connected ADC!\n")
    print("Calibrated ADC!\n")
else:
    print("Can't find the adc, exiting ...\n")
    exit()

# initialize LCD display + verify it works
lcd = LCD_I2C.lcd(bus)
lcd.lcd_display_string("Calibrating ADC", 1)

# Constants
R1 = 214.3
R2 = 215.8
R3 = 9770
VIN = 3.29
VREF = VIN / 2
VDEVIATION = (0.0166036203409, -0.0384329033931, 1.00958174262, 0.010941954783)
# unknown voltage divider seems slightly off but it varies with voltage?
EPSILON = 1e-19

ADC_MAX = 2**23
SAMPLES = 80 # how many adc readings are averaged

H = 671.63
P = -654.846
D = -0.104766
CONVERSION = lambda volt: max(0, H / (volt + D) + P)
# CONVERSION = lambda cond: 100 * cond

def main():
    # LEDs
    GPIO.setmode(GPIO.BCM)
    RedLED = LED(22, 0, 1600)
    BlueLED = LED(27, 1600, 3300)
    GreenLED = LED(17, 3300, float('Inf'))
    LEDs = [RedLED, BlueLED, GreenLED]
    
    # cool lightshow to verify LEDs work
    letThereBeLight(LEDs)

    # find Vin (callibration since batteries slowly loose voltage?)
    for _ in range(3):
        value = adc.getAverage(SAMPLES)
        VIN, _, _ = interpretAdc(value)
        VREF = VIN / 2
        print('VIN callibrates to: ' + str(VIN))

    minVout = float('inf')
    try:
        print('Reading detector values')
        while True:
            # Read the ADC for SAMPLES and return the average reading
            value = adc.getAverage(SAMPLES)

            # convert ADC value to the desired values (voltage, resistance, conductivity)
            vout, resistance, conductance = interpretAdc(value)
            conductivity = CONVERSION(vout)
          
            # print live values
            printValues(value, vout, resistance, conductivity)

            # only keep minVout
            if (vout < minVout): minVout = vout
            else: vout = minVout
            conductivity = CONVERSION(vout)
            
            # show values on LCD
            lcd.lcd_clear()
            lcd.lcd_display_string("Voltage (adc value):", 1) 
            lcd.lcd_display_string(str(round(vout)) + " (" + str(value) + ")", 2)
            lcd.lcd_display_string("Concentration (ppm):", 3) 
            lcd.lcd_display_string(str(round(conductivity)), 4)
            
            # activate LEDs
            for l in LEDs:
                l.update(conductivity)
            
            # Pause for a second
            time.sleep(1)
    finally:
        print("Clean Exit \n")
        GPIO.cleanup() # ensure clean exit

def printValues(value, vout, resistance, conductivity):

    print('ADC: ' + str(value) + #' ' + format(int(value), 'b') +
            ' | Vol: ' + str(round(vout,5)) +
            ' | Res: ' + str(round(resistance)) +
            ' | Con: ' + str(round(conductivity,4))
    )

def interpretAdc(value):
    return interpretWheatstone(value)

def interpretWheatstone(value):
    vout = VREF * value / ADC_MAX
    v12 = VIN * R2 / (R1 + R2) # voltage out at known voltage divider
    vout += VDEVIATION[0] * (vout + v12) ** 3 + VDEVIATION[1] * (vout + v12) ** 2 + VDEVIATION[2] * (vout + v12) + VDEVIATION[3] - vout - v12
    # experimentally determined adjustment factor lol
    
    print('known voltage divider: ' + str(v12) +
          ' vout: ' + str(vout)
    )
    v3x = vout + v12 # voltage out at unknown voltage divider
    resistance = R3 * (R2 * VIN + (R1 + R2) * vout) / (R1 * VIN - (R1 + R2) * vout + EPSILON)
    conductance = (R1 * VIN - (R1 + R2) * vout) / (R3 * (R2 * VIN + (R1 + R2) * vout) + EPSILON)
    return v3x, resistance, conductance

def interpretSimpleVoltageDivider(value):
    vout = VREF * value / ADC_MAX
    voutNorm = vout / VIN
    resistance = R1 * voutNorm / (1 - voutNorm + EPSILON)
    conductance = (1 - voutNorm) / (R1 * voutNorm + EPSILON) # conductivity is inverse resistivity (normalized for distance)
    return vout, resistance, conductance

def letThereBeLight(LEDs):
    for l in LEDs:
        l.on()
        time.sleep(0.3)
        l.off()
    for l in LEDs:
        l.on()
    time.sleep(0.5)
        
class LED():
    def __init__(self, pin, lower, upper):
        self.pin = pin
        self.lower = lower
        self.upper = upper
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def update(self, value):
        if value >= self.lower and value < self.upper:
            self.on()
        else:
            self.off()
    
# runs main() when program is run from terminal
if __name__ == '__main__':
    main()