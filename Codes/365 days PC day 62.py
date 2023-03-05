#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:27:38 2023

@author: boladipo
"""

 # program to find the factors of a Number
 
 
 
 # This program computes the factor of the argument passed
 
 
def print_factors(x):
    
     print(f"The factors of {x} are :")
     for i in range(1, x+1):
         if x % i ==0:
             print(i)
             
num = int(input("Enter a Number to find the Factors :"))
print_factors(num)