# sin_rad.py: Prints the sin values for 30 equidistant angle values in radians
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from math import sin,radians,pi

# define a function that returns the sin value of an angle given in degrees
def sin_deg(angle):
    return(sin(radians(angle)))
            
for i in range(37): # print the last point of the sin function as well
    angle = i*10
    print(angle,sin_deg(angle))
    
