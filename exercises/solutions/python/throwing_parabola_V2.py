# throwing_parabola.py: Calculates the trajectory of a stone thrown at speed
# v at an angle alpha
# In this version we use a constant number of points for each parabola. For this
# we first calculate the total time of the flight.
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from math import sin,cos,radians

g = 9.81          # acceleration due to gravity
alpha = 60        # angle at which the stone is thrown
v = 30            # speed in m/s
NO_OF_POINTS = 50 # number of points for which the parabola is calculated

def flight_duration(vertical_speed):
    # vt = 1/2gt**2 => t = 2v/g
    return 2*vertical_speed/g

# calculate the parabola with "no_of_points" points
# Like this we calculate the parabola from its start until the object hits ground again

def trajectory(init_speed,angle,no_of_points):
    v_hor = init_speed*cos(radians(angle)) # constant horizontal speed
    v_ver = init_speed*sin(radians(angle)) # initial vertical speed

    hor_pos = 0.0
    ver_pos = 0.0
    f_d = flight_duration(v_ver)
    # print("flight duration: ",f_d)
    t = 0
    
    for point in range(no_of_points):        
        t = f_d/(no_of_points-1) * point
        hor_pos = v_hor*t
        ver_pos = v_ver*t - g*t*t/2
        print(hor_pos,ver_pos)

trajectory(v,alpha,NO_OF_POINTS)
