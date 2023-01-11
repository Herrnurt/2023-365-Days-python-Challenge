#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 23:22:43 2023

@author: boladipo
"""

## Roman Numbers to Decimlas in Python


tallies = { 'I' : 1, 'V' : 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}


def RomanNumeralToDecimal(romanNumeral):
    
    sum = 0
    
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies [left] < tallies [right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    
    return sum
    
    
roman = input("Enter Roman Numbers : ")
RomanNumeralToDecimal(roman)
