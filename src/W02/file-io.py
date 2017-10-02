#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

file-io.py

Josh Kaplan
jk@ucf.edu

Here is a brief example of how to read and write files in Python.

"""

# To read a file, we open it. 
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()

# To write to a file, we open it with the 'w' (write) mode.
# Then use the the write function.
f = open('hello.txt', 'w')
f.write('Hello World')
f.close()

# Here's a shorthand way of doing it.
# In this case, the 'with' statement automatically closes 
# the file when we unindent
with open('hello.txt', 'r') as f:
    content = f.read()
print(content)

