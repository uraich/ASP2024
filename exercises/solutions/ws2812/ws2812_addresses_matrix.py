# ws2812_addresses.py: lights each of the 64 LEDs
# This allows to figure out, which LED corresponds to which LED address
# Copyright (c) U. Raich, 3.1.2024
# This program is part of the IoT workshop at the African School of Physics
# It is released under the MIT license

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

n    = 64 # 64 pixels on the pixel matrix
d_in = 16 # GPIO pin onto which the neo pixels are connected
intensity = 0x1f # limit the light intensiy not to blind your eyes

np = NeoPixel(Pin(d_in),n)

def clear():
    for i in range(n):
        np[i] = (0,0,0)
    np.write()
    
clear()    # clear all pixels
for i in range(n):
    print(i)
    np[i] = (0,intensity,0) # switch the LED on (red color)
    np.write()
    sleep_ms(200)
    np[i] = (0,0,0)
    np.write()
