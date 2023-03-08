#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:38:26 2023

@author: boladipo
"""

## Floyd's Triangle in Python using for loop




print("Enter the number of Rows: ", end="")



row = int(input())



num = 1

for i in range(row):
    for j in range(i +1 ):
        print(num, end=" ")
        
        num = num + 1
        
    print()
    
    