#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

exercise-5.py

Josh Kaplan
jk@ucf.edu

If we list all the natural numbers below 10 that are multiples of 3 or 5 we 
get 3, 5, 6, and 9. The sum of these multiples is 23. Write a program that 
finds the sum of all multiples of 3 or 5 below 1000.

Note: This problem comes from Project Euler (https://projecteuler.net/problem=1),
which can be a great source for some mathematical programming exercises.

"""

total = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)