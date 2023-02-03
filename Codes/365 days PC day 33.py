#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:49:25 2023

@author: boladipo
"""

## Python Code for Pascal's Triangle


def printPascal(N):
    
    
    arr = []
    temp = []
    print("pascal's triangle of", N, "Rows...")
    for i in range(N):
        print("rows", i+1, end=" : ")
        for j in range(len(arr)):
            print(arr[j], end=" ")
            
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j + 1])
            
        temp.append(1)
        arr = temp
        temp = []
        
        
N = int(input("Enter the Number for the pascal triangle :"))
printPascal(N)