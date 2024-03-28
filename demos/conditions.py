# conditions.py: Demonstrates conditions
# This is a demo shown during the lectures
# of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

a,b = 5,7
print("a: ",a," b: ",b)
if a > b:
    print("a is bigger than b")  # note that the body of the condition
                                 # is indented
                                 # all the indented code is executed if the
                                 # condition evaluates to true
elif a < b:
    print("a is smaller than b")
else:
    print("a and b are equal")
