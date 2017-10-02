#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

list-1.py

Josh Kaplan
jk@ucf.edu

Some features of lists

"""
import math

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 5, math.pi, 3, 3]
C = ['Arthur', 'Lancelot', 'Robin', 'Galahad', 'Bedevere', 'Dennis']

print('\nLength')
print(len(A))
print(len(B))
print(len(C))

print('\nAppend to Lists')
A.append(12)
print(A)
C.append('Tim')
print(C)


print('\nRemove from Lists')
A.remove(3)
print(A)
B.remove(3)
print(B)
C.remove('Robin')
print(C)

print('\nInsert into Lists')
A.insert(2, 3)
print(A)