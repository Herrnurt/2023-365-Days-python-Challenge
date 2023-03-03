#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:41:15 2023

@author: boladipo
"""


## Program for the Fibonacci Sequence



# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))


# first two terms

n1, n2, = 0, 1


count = 0
# Check if the number of terms is valid 

if nterms <= 0:
    print("Please enter a postion integer")
# if there is only one term, return n1

elif nterms == 1:
    print("Fibonacci sequqnce upto", nterms," :")
    print(n1)
    
# generate fibonacci sequqnce
else:
    print("Fibonacci sequqnce: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # upldate values
        n1 = n2
        n2 = nth
        count += 1