#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

functions-1.py

Josh Kaplan
jk@ucf.edu

How about a more mathematical example.

"""

def freefall_dist(time):
    g = 9.81
    t = time
    y = 0.5 * g * t**2
    return y

print('Time (s)    Dist (m)')
print('--------    --------')

t = 2
d = freefall_dist(t)
print('{:6.1f} s {:8.1f} m'.format(t, d))

t = 5
d = freefall_dist(t)
print('{:6.1f} s {:8.1f} m'.format(t, d))

t = 10
d = freefall_dist(t)
print('{:6.1f} s {:8.1f} m'.format(t, d))
