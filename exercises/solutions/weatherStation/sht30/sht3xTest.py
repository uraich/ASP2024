# sht3xTest.py is a program to exercise the sht3x module, a driver for
# the SHT30 temperature and humidity sensor
# Copyright (c) U. Raich, May 2020
# The program was written for the course on the Internet of Things
# at the University of Cape Coast, Ghana
# It is released under GPL

# import the SHT3X class
from sht3x import SHT3X,SHT3XError
import sys,time
    
# create a SHT3X object
try:
    sht30 = SHT3X()
except SHT3XError as exception:
    if exception.error_code == SHT3XError.BUS_ERROR:
        print("SHT30 module not found on the I2C bus, please connect it")
        sys.exit(-1)
    else:
         raise exception
        
# read out the serial number
print("Serial number: 0x{:02x}".format(sht30.serialNumber()))

# demonstrate a single shot measurement with clock-stretching
print("Measure with clock stretching")
while True:
    tempC, humi = sht30.getTempAndHumi()
    print("Temperature: ",tempC,"°C, Humidity: ",humi,"%")
    time.sleep(1)
