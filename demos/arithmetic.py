# arithmetic.py: Demonstrates basic arithmetic operations
# This is a demo shown during the lectures
# of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

s=5+7
a=5
b=7
sum = a+b
difference = a-b
product = a*b
division = a/b    # yields a float value
div_int  = a//b   # yields an integer division,
                  # only integer part of the division is taken
                  # into account

print("s: ",s)
print("5 + 7 =",sum)
print("5 * 7 =",product)
print("float division: a / b = ",division)
print("integer division: a // b = ",div_int)
