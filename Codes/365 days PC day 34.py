#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:42:35 2023

@author: boladipo
"""

## Full Diamond Pattern in Python



rows = int (input("enter Diamond Pattern Rows :"))

print("Diamond Star Patterns")

for i in range (1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end =" ")
    for k in range(0, 2 * i -1):
        print('*', end='')
        
    print()
    
    
for i in range(1, rows):
    for j in range(1, i + 1):
        print(end=' ')
    for l in range(1, (2 * (rows -i))):
        print('*', end='')
    print()