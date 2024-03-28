# damped_osc.py: Calculates the shape of a damped oscillator
# The values can be saved on a file by redirecting stdout to a file
# After that the data are plotted with gnuplot
# This is a demo shown during the lectures
# of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license


from math import sin,exp

def func(x):
    return exp(-x/10)*sin(x)

for i in range(500):
    print(i/10,func(i/10))
