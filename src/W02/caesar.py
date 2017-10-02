#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

caeser.py

Josh Kaplan
jk@ucf.edu

A Caeser cipher is a technique for encrypting data.


"""

import string

ROT = 1

def encrypt(msg):
    # For simplicity, let's only deal with uppercase
    msg = msg.upper()    
    letters = string.ascii_uppercase
    
    # Now let's determine our encrypted message
    encrypted_msg = ''
    for c in msg:
        index = (letters.find(c) + ROT) % 26  # The index of our new letter in letters
        new_letter = letters[index]           # The new letter itself
        encrypted_msg += new_letter
    return encrypted_msg

def decrypt(encrypted_msg):
    # For simplicity, let's only deal with uppercase
    encrypted_msg = encrypted_msg.upper()    
    letters = string.ascii_uppercase
    
    # Now let's determine our encrypted message
    msg = ''
    for c in encrypted_msg:
        index = (letters.find(c) - ROT) % 26  # The index of our new letter in letters
        new_letter = letters[index]           # The new letter itself
        msg += new_letter
    return msg

enc = encrypt('ABC')
print(enc)
dec = decrypt(enc)
print(dec)