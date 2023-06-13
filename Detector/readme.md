# Detector Building 2021-2022
This Science Olympiad event was centered around electrical engineering and chemistry with the building portion being focused on designing and building a conductivity meter to measure salt concentration from 0 to 5000 ppm. We had to build everything from scratch using only basic circuit components and DIP. More information on the science here: https://publiclab.org/wiki/conductivity_sensing

![detector](https://github.com/SanderGi/Science-Olympiad/assets/97496861/d804d9ef-6f6d-4cb0-8567-a7f1ebf89cf2)

## What I did
I created a dual voltage divider circuit (similar to a Wheatstone bridge) to measure the voltage drop in a fixed distance (and at a fixed submersion) of the fluid using a differential ADC (namely the NAU7802). I then implemented a driver to interface with this ADC over the I2C protocol on my Raspberry Pi and implemented a curvefitting program to callibrate the sensor to convert voltage readings to salt concentration in ppm.

Read the [https://github.com/SanderGi/Science-Olympiad/blob/main/Detector/C05_DetectorBuilding_SpecSheet.docx](specsheet) for a technical breakdown of my circuit, sensor and program.

## Some challenges I had to overcome
- Noisy data: Tackled by creating a regulated reference voltage and callibrating the ADC for natural sensor decline and variability, plus higher ADC sample rate to use digital processing to smooth out most of the noise
- The voltage affecting the concentration reading over time: quicker measurements based on a minimum voltage drop instead of a moving average
- Screen flickering and ADC crashing (at higher sample rates): implement a custom battery powered power supply with voltage regulators (since we couldn't use the wall outlet per event rules)
- The ADC chips supporting Raspberry Pi don't have enough resolution (only 10 bits = 1024 values < the 5000 ppm's we were tasked with identifying): implement custom drivers for the NAU7802 chip.
- Implementing a custom power supply to power the screen and ADC at a higher sample rate (more detailed signal => better output)
