# -*- coding: utf-8 -*-
"""

conditions-1.py

Josh Kaplan
jk@ucf.edu

An example of an if/elif/else condition,

"""

# Get a number from the user
x = int(input('Enter a number: '))

if x > 0:
    print('You entered a positive number!')
elif x < 0:
    print('You entered a negative number!')
else:
    print('You entered zero!')

