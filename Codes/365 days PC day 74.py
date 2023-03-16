#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:40:08 2023

@author: boladipo
"""



## Python Program for Disarium Number


Number = int(input("enter the Number to check Diarium Number = "))

length = len(str(Number))

Temp = Number 
Sum = 0
rem = 0 

while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem ** length)
    Temp = Temp // 10
    length = length -1
    
    
    
    
print("The Sum of the Digits = %d" %Sum)

if Sum == Number:
    print("\n%d is a Disarium Number. " %Number)
else:
    print("%d is not a Disarium Number , "%Number)