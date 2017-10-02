#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

int-2.py

Josh Kaplan
jk@ucf.edu

Here are some examples of printing integers.

"""

x = 5
y = 10

print('\nDecimal Examples')
print('1. {:d}'.format(x))
print('2. {:02d}'.format(x))
print('3. {:020d}'.format(x))

print('\nHexadecimal Examples')
print('4. {:x}'.format(y))
print('5. {:X}'.format(y))
print('6. 0x{:02X}'.format(y))

print('\nBinary Examples')
print('7. 0b{:b}'.format(x))
print('8. {:08b}'.format(x))
print('9. {:08b}'.format(y))

# This is older way of printing values in Python
# It's still a valid and is often easier to read. 
# But it's less powerful. For example, it won't support binary printing.
print('\nAn Older Style of Printing')
print('10. %d' % x)
print('11. %02d' % (x))
print('12. %02X' % y)       