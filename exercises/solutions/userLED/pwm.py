# pwm.py: Periodically changes the light intensity on the user LED using pwm
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from machine import Pin,PWM
from time import sleep_ms
LED_PIN = 2

led = PWM(Pin(LED_PIN))

while True:
    for i in range(1024):
          led.duty(i)
          sleep_ms(2)
    for i in range(1023,-1,-1):
          led.duty(i)
          sleep_ms(2)
    
