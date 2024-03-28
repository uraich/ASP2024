# pb_state.py: Reads and prints the state of the pushbutton every 100 ms
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from machine import Pin
from time import sleep_ms

PB_PIN = 17 # the push button is connected to this pin

pb = Pin(PB_PIN,Pin.IN, Pin.PULL_UP) # program the pin to be input  and
                                     # add the pull up resistor
while True:
    if (pb.value()):  # if we get a one here, we see the pullup resistor
                      # this means that the switch is open
        print("Push button is released")
    else:             # if we read zero, the switch is grounded
                      # this means it must be pressed
        print("Push button is pressed") 
    sleep_ms(100)
