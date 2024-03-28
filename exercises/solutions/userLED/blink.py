# blink.py: The ubiquous hello world program for embedded system: a program
# blinking a LED. The user programmable LED on the CPU card is used
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from machine import Pin
from time import sleep_ms
LED_PIN = 2

led = Pin(LED_PIN,Pin.OUT)

while True:
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)
    
