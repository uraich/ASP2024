# fibonacci.py: a program that calculates the Fibonacci number series
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

N = 20

# a function calculating the Fibonacci numbers up to F(n)
# normally we should check for negative numbers here, but I decided to skip this check

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            F = a+b
            a = b
            b = F
    return F

for n in range(N+1):
    print("F(",n,") = ",fibonacci(n))
    
    # This is a little nicer, but we have not seen formatted output during the lectures
    # print("F({:d}) = {:d}".format(n,fibonacci(n))) 

