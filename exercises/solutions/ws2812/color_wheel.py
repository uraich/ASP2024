# color_wheel.py: lights a ring of LEDs in the colors of the rainbow
# Copyright (c) U. Raich, 3.1.2024
# This program is part of the IoT workshop at the African School of Physics
# It is released under the MIT license

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

pixels = [59,58,49,40,32,24,16,9,2,3,4,5,14,23,31,39,47,54,61,60]
n    = 64 # 64 pixels on the pixel matrix
d_in = 16 # GPIO pin onto which the neo pixels are connected
intensity = 0x1f # limit the light intensiy not to blind your eyes

np = NeoPixel(Pin(d_in),n)

def clear():
    for i in range(n):
        np[i] = (0,0,0)
    np.write()
    
clear()    # clear all pixels

print("We use {:d} pixels".format(len(pixels)))
for i in range(len(pixels)):
    np[pixels[i]] = (0,intensity,0)
np.write()
sleep_ms(5000)
clear()
