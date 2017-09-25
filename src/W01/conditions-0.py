# -*- coding: utf-8 -*-
"""

conditions-0.py

Josh Kaplan
jk@ucf.edu

An example of an if/else condition,

"""

# Get a number from the user
x = float(input('Enter a number: '))

if x > 0:
    print('You entered a positive number!')
elif x == 0:
    print('you entered zero!')
else:
    print('You entered a negative number!')