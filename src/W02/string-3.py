#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

string-3.py

Josh Kaplan
jk@ucf.edu

Let's have some fun with printing and strings.

https://docs.python.org/3/library/string.html#format-string-syntax

"""

x = 4e9
spaces = 12
places = spaces - 2

fmt = 'pi = {{:{:d},.{:d}f}}'.format(spaces, places)
print(fmt)

s = fmt.format(x)
print(s)
