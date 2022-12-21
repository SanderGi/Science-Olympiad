# Detector Building 2021-2022
This Science Olympiad event was centered around electrical engineering and chemistry with the building portion being focused on designing and building a conductivity meter to measure salt concentration from 0 to 5000 ppm. We had to build everything from scratch using only basic circuit components and DIP. More information on the science here: https://publiclab.org/wiki/conductivity_sensing

## What I did
I created a dual voltage divider circuit (similar to a Wheatstone bridge) to measure the voltage drop in a fixed distance (and at a fixed submersion) of the fluid using a differential ADC (namely the NAU7802). I then implemented a driver to interface with this ADC over the I2C protocol on my Raspberry Pi and implemented a curvefitting program to callibrate the sensor to convert voltage readings to salt concentration in ppm.
