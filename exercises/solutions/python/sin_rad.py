# sin_rad.py: Prints the sin values for 30 equidistant angle values in radians
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from math import sin,pi

for i in range(31): # print the last point of the sin function as well
    angle = 2*pi*i/30
    print(angle,sin(angle))
    
