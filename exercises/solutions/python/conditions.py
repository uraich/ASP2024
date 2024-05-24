# conditions.py: Demonstrated conditions on Python
# This is part of the course of small physics experiments at the
# African School of Funcamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

numberString = input("Please give two numbers: ")
numbers = numberString.split(" ")
a = int(numbers[0])
b = int(numbers[1])

if a > b:
    print(a,"is bigger than",b)
elif a < b:
    print(a,"is smaller than",b)
else:
    print(a,"and",b,"are equal")