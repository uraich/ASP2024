# loops.py: Demonstrates loops in Python
# This is a demo shown during the lectures
# of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license


print("for loop")
for i in range(5):
    print("Hello World")  # prints “Hello World” 5 times)

print("while loop with 'while i > 5'")
i = 5
while i > 0:
    print("Hello World")  # does the same thing 
    i -= 1                # different syntax for i= i – I

'''
This is a multi-line comment. I put this because otherwise we would
never see the next loop

while True: 
	print("Hello World!")  # will print forever
'''

print("endless while loop with break")
i=5
while True:
   print("Hello World")
   i -= 1
   if i == 0:
       break              # breaks out of the loop
