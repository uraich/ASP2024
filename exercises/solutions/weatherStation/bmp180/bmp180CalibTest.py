#!/usr/bin/python3.5
#
# This is the Python example using the bmp180 class
# barometric pressure sensor
# 2-line LCD display
# U. Raich UCC, Nov.2017

from Bmp180Class import Bmp180

bmp180 = Bmp180()
bmp180.setDebug(True)
oss = bmp180.getResolution()
print("in main: resolution is: ",oss)
print("chip id: %02x"%bmp180.chipID())
print("calibration values: ", bmp180.getCalib())
bmp180.setUncompensatedTestValues()
bmp180.dummyCalib()
bmp180.convert()
print("temperature  = " + str(bmp180.getTemperature())+"°C")
print("air pressure = " + str(bmp180.getPressure())+"hPa")
