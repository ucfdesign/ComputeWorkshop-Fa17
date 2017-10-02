#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

int-1.py

Josh Kaplan
jk@ucf.edu

Let's play around with division.

"""

x = 3
y = 4

# Python 3 does floating point division by default
z = x/y
print(z, type(z))

# You can use // do explicitly do integer division
z = x//y
print('z = {} of type {}'.format(z, type(z)))