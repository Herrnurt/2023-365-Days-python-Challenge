#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:28:21 2023

@author: boladipo
"""



## Star Pattern Diffrence Shapes using Python




# 1. Print a triangle of Stars
 
 
rows = 6
 
for i in range(rows):
    for j in range(i+1):
        print('*', end = '')
    print()
    
    
# 2 Print an inverted traingles of stars


rows = 7
for i in range(rows, 0 , -1):
    for j in range(0, i):
        print('*', end = '')
        
    print()
    
    

# 3 Print  a diamon of stars


rows = 5


for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end = '')
    for k in range(1, 2*i):
        print('*' , end ='')
    print()
    
for i in range(rows-1, 0,  -1):
    for j in range(1, rows-i+1):
        print(' ', end = '')
    for k in range(1, 2*i):
        print('*' , end ='')
    print()