#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:59:36 2023

@author: boladipo
"""

## Python program to Generate Password


# Import random module
import random

# user input for password lengyh
passlen = int(input("Enter the lengths of password : "))


# Storing letters, numbers and special characters
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"


# random sampling by joining the length of the password and the varaiable s
p = " ".join(random.sample(s, passlen))

print(p)



