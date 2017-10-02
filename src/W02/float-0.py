#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

float-0.py

Josh Kaplan
jk@ucf.edu

Here is a brief intro to floating point numbers or 'floats' for short.

"""

import math

x = 3.0
y = 4.0

print('x is a {}. It\'s value is {}'.format(type(x), x))
print('y is a {}. It\'s value is {}\n'.format(type(y), y))

z = x + y
print('z is a {}. It\'s value is {}\n'.format(type(z), z))

z = x*y
print('z is a {}. It\'s value is {}\n'.format(type(z), z))

z = x/y
print('z is a {}. It\'s value is {}\n'.format(type(z), z))

z = math.sqrt(x**2 + y**2)
print('z is a {}. It\'s value is {}'.format(type(z), z))

