#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

string-1.py

Josh Kaplan
jk@ucf.edu

Some examples with Python's string library
See Also: https://docs.python.org/3/library/string.html

"""

# Import the string library
import string


# Here, we convert the integer 10 to a string
s1 = str(9)     
s2 = 'ABC'
s3 = 'A'

print(s1, type(s1).__name__)

print('\nSome useful things in the string module')
print(string.ascii_letters)
print(string.digits)

print('\nSome Boolean Expressions')
print(s1 in string.digits)
print(s2 in string.digits)
print(s2 == 'ABC')

print('\nBoolean Expressions - Individual Characters')
print(s3 == 65)             # Try this one in C, do you get the same result?
print(s3 == chr(65))
print(s3 < 'B') 
