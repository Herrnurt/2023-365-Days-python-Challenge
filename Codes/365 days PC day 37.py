#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:43:26 2023

@author: boladipo
"""




## Sequence Matcher In Python 




from difflib import SequenceMatcher 

text1 = input ("Enter 1st sentence : ")
text2 = input("Enter 2nd setence : ")


sequenceScore = SequenceMatcher(None, text1, text2).ratio()


print(f"Both are {sequenceScore * 100} % similar ")
      
      
      