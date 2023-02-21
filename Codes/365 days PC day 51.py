#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:40:15 2023

@author: boladipo
"""



# perfect Number verification in Python


def perfectNumber(number):
    sum = 0
    for x in range(1, number):
        if number % x==0:
            sum += x
            
    return sum ==number

if __name__ == '__main__':
    
    
    n = int(input("Enter a number to check :"))
    print(perfectNumber(n))