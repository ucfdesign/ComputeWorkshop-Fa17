#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

int-0.py

Josh Kaplan
jk@ucf.edu

Here is a brief intro to integers.In this case, we define two integers x and y.
We then create another variable called z. Let's try a few different ways of 
calculating z. What is it's type? 

Do we get the same results in Python 2?
What about C or MATLAB?

"""

import math

x = 3
y = 4

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