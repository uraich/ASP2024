# throwing_parabola.py: Calculates the trajectory of a stone thrown at speed
# v at an angle alpha
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from math import sin,cos,radians

g = 9.81    # acceleration due to gravity
alpha = 80  # angle at which the stone is thrown
v = 30      # speed in m/s
time_resolution = 0.1 # time resolution in s

def trajectory(init_speed,angle,time_resolution):
    v_hor = init_speed*cos(radians(angle)) # constant horizontal speed
    v_ver = init_speed*sin(radians(angle)) # initial vertical speed

    hor_pos = 0.0
    ver_pos = 0.0
    t = 0
    print(hor_pos,ver_pos)
    while ver_pos >= 0:
        t += time_resolution
        hor_pos = v_hor*t
        ver_pos = v_ver*t - g*t*t/2
        print(hor_pos,ver_pos)

trajectory(v,alpha,time_resolution)
