#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

float-1.py

Josh Kaplan
jk@ucf.edu

Let's do a bit more with floats. Notice we can use add '.__name__' to our
type check to clean it up a bit.

"""

import math

r = 3.0
c = 2*math.pi*r

print('r is a {}. It\'s value is {}'.format(type(r).__name__, r))
print('c is a {}. It\'s value is {}'.format(type(c).__name__, c))


