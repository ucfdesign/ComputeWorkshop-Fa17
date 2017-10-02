#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

list-2.py

Josh Kaplan
jk@ucf.edu

Let's try out some loops with lists

"""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = ['Arthur', 'Lancelot', 'Robin', 'Galahad', 'Bedevere', 'Dennis']

print('\nLength')
print(len(A))
print(len(B))

print('\nHere is an example of looping through a list:')
for i in range(0, len(A)):
    # Let's only print a new line for the last item
    # Otherwise, we print a comma
    # 
    # As an aside, shorter way to write this is:
    # end_string = '\n' if (i == len(A) - 1) else ', '
    if i == len(A) - 1:
        end_string = '\n'
    else:
        end_string = ', '
        
    # Print the item
    print(A[i], end=end_string)
    
print('\nHere is another example:')
for person in B:
    print(person)
    
print('\nHere is a troublesome example:')
for person in B:
    if person == 'Robin':
        B.remove(person)
    print(person)
    
B = ['Arthur', 'Lancelot', 'Robin', 'Galahad', 'Bedevere', 'Dennis']
print('\nHere is a better approach:')
for i, person in enumerate(B):
    print(i, end=' ')
    if B[i] == 'Robin':
        B.remove(B[i])
    print(person, end=' ')
    print(B[i])
