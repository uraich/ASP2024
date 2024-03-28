# weatherStation.py: Reads temperature and humidity from the SHT30
# and the barometric pressure from the BMP180
# Displays the result on the OLED display
# Copyright (c) U. Raich, March 2024
# This program is part of the workshop of small physics labs at the
# African School of Physics
# It is released under the MIT license

import sys
from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
from Bmp180Class import Bmp180
from sht3x import SHT3X,SHT3XError
from utime import sleep

print("Running on ESP32") 
scl = Pin(22)   # on the wemos d1 mini (esp32) scl is connected to GPIO 22
sda = Pin(21)   # on the wemos d1 mini (esp32) sda is connected to GPIO 21
i2c = I2C(1,scl=scl,sda=sda)

print(i2c)

# create a SHT3X object
try:
    sht30 = SHT3X()
except SHT3XError as exception:
    if exception.error_code == SHT3XError.BUS_ERROR:
        print("SHT30 module not found on the I2C bus, please connect it")
        sys.exit(-1)
    else:
         raise exception

# create a BMP180 object     
bmp180 = Bmp180()

# create an object of class SSD1306 defined in ssd1306.py
# the driver is already included in the MicroPython interpreter

# print the frame text on the display
ssd1306 = SSD1306_I2C(128,64,i2c)
ssd1306.text("Weather Station",0,0,1)
ssd1306.text("Temp :         C",0,20,1)
ssd1306.text("Humidiy:      %",0,30,1)
ssd1306.text("Press:        hP",0,40,1)
ssd1306.show()
tString = None
hString = None

while True:
    # get temperature and humidity from the SHT30
    tempC, humi = sht30.getTempAndHumi()
    print("Temperature: ",tempC,"°C, Humidity: ",humi,"%")
    print("temperature (SHT30): " + str(tempC)+"°C")
    print("relative humidity:   " + str(humi)+"%")

    # get the air pressure from the BMP180
    bmp180.measure()
    bmp180.convert()
    print("temperature (BMP180): " + str(bmp180.getTemperature())+"°C")
    print("air pressure: " + str(bmp180.getPressure())+"hPa")
    
    # remove old results from the display 
    if tString:
        ssd1306.text(tString,12*6,20,0)
        ssd1306.text(hString,12*6,30,0)
        ssd1306.text(hString,12*6,40,0)        
    # write the results to the display        
    tString = "{:5.2f}".format(tempC)
    hString = "{:5.2f}".format(humi)
    pString = "{:5.1f}".format(bmp180.getPressure())
    ssd1306.text(tString,12*6,20,1)
    ssd1306.text(hString,12*6,30,1)
    ssd1306.text(pString,12*6,40,1)    
    ssd1306.show()
    sleep(1)
