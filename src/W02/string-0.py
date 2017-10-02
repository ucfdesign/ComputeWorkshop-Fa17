#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

string-0.py

Josh Kaplan
jk@ucf.edu

Some examples with strings
See Also: https://docs.python.org/3/library/string.html

"""

s1 = 'Thou shalt count to 3'
s2 = 'Ni'

print(s1)
print(s1.upper())           # We can make a string uppercase
print(s1.lower())           # Or lowercase
print(s1.title())           # Or capitalize the first letter of each word

print(s2 + ' ' + s2 + '!')
print('{} {}!'.format(s2, s2))
print('{MyString} {MyString}!'.format(MyString=s2))

