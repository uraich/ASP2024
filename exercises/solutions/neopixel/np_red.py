# neopixel.py: Lights each LED of the ws2812 LED ring in red to find out which
# LED number corresponds to which physical LED
# Copyright U. Raich 2022
# The program is part of African School of Physics 2022

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

NEOPIXEL_PIN = 26
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),7)

red  = (31,0,0)
dark = (0,0,0)

for i in range(7):
    neopixel[i] = red
    neopixel.write()
    sleep_ms(500)
    neopixel[i] = dark
    sleep_ms(500)
    neopixel.write()

