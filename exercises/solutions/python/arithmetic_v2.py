# arithmetic.py: A simple program demonstrating assignment in Python and the four
# basic arithmetic operations addition, subtraction, multiplication, division
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U. Raich
# The program is released under the MIT license

numberString=input("Please give two numbers: ")
# input return the string of what you typed
numbers=numberString.split(" ")
# If you separated the numbers by a space you can split the string into 2
# and you can convert the string into an integer
a = int(numbers[0])
b = int(numbers[1])
print(a,b)
sum = a+b
difference = a-b
product = a*b
floatDivision = a/b
integerDivision = a//b
print(a,"+",b,"=",sum)
print(a,"+",b,"=",sum)
print(a,"*",b,"=",product)
print(a,"/",b,"=",floatDivision,"float Division")
print(a,"//",b,"=",integerDivision,"integer Division")