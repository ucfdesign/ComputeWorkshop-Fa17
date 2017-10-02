#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

file-io.py

Josh Kaplan
jk@ucf.edu

Let's do another example of reading a file, but this time let's accept
a command-line argument'

"""

import sys

args = sys.argv
print(args)

if len(args) != 2:
    print('Usage: python command-line.py <filename>')
    exit()

# If we don't specifiy the 'r' mode, Python assumes we mean to read the file.
with open(args[1]) as f:
    content = f.read()
    
print(content)

