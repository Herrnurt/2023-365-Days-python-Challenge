#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:14:50 2023

@author: boladipo
"""

## 

color = ["Black", "Brown", "Red", "Orange", "yellow", "Green", "Blue", "Violet",
         "Grey", "White"]


n = color.index(input("Enter the ist color :"))
m = color.index(input("enter the 2nd color :"))
p = color.index((input("Enter the 3rd color")))



q = int(((n*10) + (m)) * (10**(p)))

z = q/1000


print("\nThe Resistance Value is :")
print(f"{q}ohms and in kiloohms : {z}kiloohms")
