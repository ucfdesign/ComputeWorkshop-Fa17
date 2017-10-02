# -*- coding: utf-8 -*-
"""

exercise-3.py

Josh Kaplan
jk@ucf.edu

Write a program that determines if a number is positive or negative. 
What should you do if the number is zero?

"""

x = float(input('Enter a number: '))

if x < 0:
    print('It\'s negative!')
elif x > 0:
    print('It\'s positive!')
else:
    print('It\'s zero!')