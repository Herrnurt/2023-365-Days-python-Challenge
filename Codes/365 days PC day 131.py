#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:43:59 2023

@author: boladipo
"""



### Converts IPv4 to integer using Python





ip = input ("ENter your IP :")

def convert(s: str):
    # Extract each digit from s
    digits = [int(x) for x in s.split('.')]
    
    # add them together
    shift = [24, 16, 8, 0]
    for i in range(4):
        digits[i] <<= shift[i]
        
    return sum(digits)

result = convert(ip)
print(result)