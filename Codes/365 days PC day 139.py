#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:37:43 2023

@author: boladipo
"""





### Converts s number to its equivalent word using Python



num = int(input("ENter a Number :"))


def number_to_words(num):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven". "eight",
             "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen" ]
    tens["", "", "twenty", "thirty", "forty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    
    
    
    
    if num < 20:
        return units(num)
    elif num < 100 :
        return tens[num // 10 ] + ('' if num % 10 == 0 else ' ' + units[num%10])
    elif num < 1000:
        return units[num // 100] + "hundred" + (''if num % 100 == 0 else ' ' + number_tp_words(num % 100))
    
    elif num < 1000000:
        return number_to_words(num // 1000) + " thousand" + ('' if num % 1000 == 0 else ' ' + numbers_to_words(num % 100))
    
    
    else: 
        return "Number out of range."
    
    
print(number_to_words)