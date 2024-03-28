# weather_display.py: A test program for the OLED 0.66' TFT display
# It shows dummy results for temperature, humidity and air pressure as
# needed for the weather station
# Copyright (c) U. Raich, December 2024
# This program is part of the workshop of small physics labs at the
# African School of Physics
# It is released under the MIT license

import sys
from ssd1306 import SSD1306_I2C
from machine import I2C,Pin

print("Running on ESP32") 
scl = Pin(22)   # on the wemos d1 mini (esp32) scl is connected to GPIO 22
sda = Pin(21)   # on the wemos d1 mini (esp32) sda is connected to GPIO 21
i2c = I2C(1,scl=scl,sda=sda)

print(i2c)
# create an object of class SSD1306 defined in ssd1306.py
# the driver is already included in the MicroPython interpreter

ssd1306 = SSD1306_I2C(128,64,i2c)
ssd1306.text("Weather Station",0,0,1)
ssd1306.text("Temp :   26deg",0,20,1)
ssd1306.text("Humidiy: 58%",0,30,1)
ssd1306.text("Pressure:1023hP",0,40,1)
ssd1306.show()
