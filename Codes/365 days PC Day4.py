#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 21:52:57 2023

@author: boladipo
"""

def least_commom_multiple(a, b):
    
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0)  and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
        
    return lcm


a = int(input("Enter ist number: "))
b = int(input("Enter second number: "))

print(least_commom_multiple(a, b))