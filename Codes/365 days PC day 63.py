#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:28:01 2023

@author: boladipo
"""

## Remove punctuation from a string




# define puctuations

punctuations = '''""''<>,./?;:=+-_()*&^%$#@!'''

my_str = input("Enter your string : ")


# To take input from the user


# remove puction from the string

no_punct = " "

for char in my_str:
    if char in punctuations:
        no_punct = no_punct + char
        
# display the unpunctuated string
print(no_punct)
    