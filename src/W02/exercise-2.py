# -*- coding: utf-8 -*-
"""

exercise-2.py

Josh Kaplan
jk@ucf.edu

Some Python examples implementing exercise 2 from last week.

"""

print('-------------------------------------------------')

# Here we convert binary and decimal numbers to integers 
print(int('10'))
print(int('10', 2))

print('-------------------------------------------------')

# Now we convert some hex numbers to integers
print(int('a', 16))
print(int('ff', 16))

print('-------------------------------------------------')

# Let's convert a few bytes into meaningful information
data = [0b01010101, 0b001000011, 0b01000110]
for b in data:
    print(chr(b), end='')
print('')
