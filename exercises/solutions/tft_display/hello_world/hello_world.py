# hello_world.py: Prints "Hello World!" on the TFT display

# Copyright (c) U. Raich, March 2024
# This program is part of the workshop of small physics labs at the
# African School of Physics
# It is released under the MIT license

from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello, World!', 0, 0, 1)
display.show()
