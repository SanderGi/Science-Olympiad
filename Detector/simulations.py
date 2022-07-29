import numpy as np
import matplotlib.pyplot as plt

# inputs
ppm = np.linspace(0, 5000, 5001) # NaCl concentration in ppm from 0 to 5000 ppm
EC = 0.000002 * ppm # Conductivity in mho/cm
resistances = 1 / EC # Resistance in ohms (assuming 1 cm probe)

# plt.plot(ppm, resistances)
# plt.xlabel("NaCl concentration (ppm)")
# plt.ylabel("Resistance (ohm)")
# plt.title("Relationship between NaCl Concentration and Resistance in water")

# electrical components
def read_adc_voltagedivider(R2, R1, VIN, VREF, MAX):
    return read_adc(VIN * R2 / (R2 + R1), VREF, MAX)

def read_adc(voltage, VREF, MAX):
    value = round(MAX * voltage / VREF)
    return max(min(value, MAX), 0) # limit value between 0 and MAX

# circuit options
def SimpleVoltageDivider(resistance, VIN = 3.3, VREF = 3.3, EPSILON = 1e-9, ADC_MAX = 1023, RREF = 10000):
    adc = read_adc_voltagedivider(resistance, RREF, VIN, VREF, ADC_MAX)
    vout = VREF * adc / ADC_MAX
    vnorm = vout / VIN
    return vnorm * RREF / (1 - vnorm + EPSILON)

def InverseVoltageDivider(resistance, VIN = 3.3, VREF = 3.3, EPSILON = 1e-9, ADC_MAX = 1023, RREF = 10000):
    adc = read_adc_voltagedivider(RREF, resistance, VIN, VREF, ADC_MAX)
    vout = VREF * adc / ADC_MAX
    vnorm = vout / VIN
    return (1 - vnorm) * RREF / (vnorm + EPSILON)

def VariableRrefVoltageDivider(resistance, VIN = 3.3, VREF = 3.3, EPSILON = 1e-9, ADC_MAX = 1023):
    changed = True
    Rref = 5000
    while changed:
        changed = False
        estimate = SimpleVoltageDivider(resistance, VIN, VREF, EPSILON, ADC_MAX, RREF=Rref)
        # uncertainty = (MAX * voltage / VREF % 1)
    return estimate

def PWMVoltageDivider():
    return 'not implemented'

def WheatstoneBridge():
    return 'not implemented'

# =============== GRAPH RESULTS ====================
# Simple test plot
predictedResistance_voltagedivider = np.array([SimpleVoltageDivider(resistance) for resistance in resistances])
residResistance_voltagedivider =  resistances - predictedResistance_voltagedivider
residPpm_voltagedivider = 500000 / resistances - 500000 / predictedResistance_voltagedivider

plt.plot(ppm, 500000 / predictedResistance_voltagedivider)
plt.title("Simple Voltage Divider and ADC")
plt.xlabel("Actual ppm")
plt.ylabel("Predicted ppm")

# Voltage Divider with various reference resistances
def SubplotPredictedAndResidual(circuitFX, title = "Voltage Divider with various Rref",  Rrefs = [1000,10000,20000]):
    fig, axs = plt.subplots(1,3)
    fig.suptitle(title)
    for Rref in Rrefs:
        axs[0].plot(ppm, 500000 / np.array([circuitFX(resistance, RREF=Rref) for resistance in resistances]))
    axs[0].set_xlabel("Actual ppm")
    axs[0].set_ylabel("Predicted ppm")
    axs[0].legend([str(Rref) + " Ohm Rref" for Rref in Rrefs])

    for Rref in Rrefs:
        axs[1].plot(ppm, 100 - 50000000 / np.array([circuitFX(resistance, RREF=Rref) for resistance in resistances]) / ppm)
    axs[1].set_xlabel("Actual ppm")
    axs[1].set_ylabel("Residual ppm as percent of actual ppm")
    axs[1].legend([str(Rref) + " Ohm Rref" for Rref in Rrefs])

    for Rref in Rrefs:
        axs[2].plot(ppm[0:100], 100 - 50000000 / np.array([circuitFX(resistance, RREF=Rref) for resistance in resistances[0:100]]) / ppm[0:100])
    axs[2].set_xlabel("Actual ppm")
    axs[2].set_ylabel("Residual ppm as percent of actual ppm")
    axs[2].legend([str(Rref) + " Ohm Rref" for Rref in Rrefs])

SubplotPredictedAndResidual(SimpleVoltageDivider, Rrefs=[10, 1000,10000])

# Inverse Voltage Divider with various reference resistances
SubplotPredictedAndResidual(InverseVoltageDivider, title="Inverse Voltage Divider with various Rref")

plt.show()