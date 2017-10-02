#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

list-0.py

Josh Kaplan
jk@ucf.edu

Some examples of lists.

"""

import math

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1.2, 1, 3, math.pi, 7]
C = ['This is a string', 'in a list', 'with some numbers', 3, 2, 1]

print(A)
print(B)
print(C)

print('')
print('Here are some examples of list indexing')
print('A[0]     =', A[0])
print('B[3]     =', B[3])
print('A[1:3]   =', A[1:3])        # Grab items 1 up to (but not including) 3
print('B[-1]    =', B[-2])         # Grab the second item from the end
print('A[1:]    =', A[1:])         # Grabs item 1 onward
print('A[:4]    =', A[:4])         # Grabs items 0 up to 4
print('A[1:8:2] =', A[1:8:2])      # Items 1 to 8, every other item
print('A[::2]   =', A[::2])        # Grab every other item
print('B[::-1]  =', B[::-1])       # Grab every item, backwards

