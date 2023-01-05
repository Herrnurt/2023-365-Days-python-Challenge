#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 02:34:16 2023

@author: boladipo
"""

## Count Character Ocurrence in Python

def count_characters(s):
    
    """ Count Characters occurence in python
    input = " string"
    output = dictionary
    
    """
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    print(count)


word = input("Enter your string: ")
print(count_characters(word))