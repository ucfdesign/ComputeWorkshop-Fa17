#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

exercise-4.py

Josh Kaplan
jk@ucf.edu

Write a program that determines if a number is even or odd. 
Hint: Look up Python’s % (modulo) operator.

"""

x = int(input('Enter a number: '))

if x % 2 == 0:
    print('You entered an even number!')
else:
    print('You entered an odd number!')