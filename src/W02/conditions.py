#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

conditions.py

Josh Kaplan
jk@ucf.edu

Here is an example of if/elif/else conditions in Python.

"""

x = 10

if x % 2 == 0:
    print('You entered an even number!')
elif x < 10:
    print('x is less than 10!')
elif x > 10 and x < 20:
    print('x between 10 and 20!')
else:
    print('You entered an odd number!')

