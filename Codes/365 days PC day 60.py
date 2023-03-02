#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 23:40:56 2023

@author: boladipo
"""

## Program to Check Armstrong Number


# take input from thr user

num = int(input("Enter a number: "))



# initialize sum

sum = 0


# fimd the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")