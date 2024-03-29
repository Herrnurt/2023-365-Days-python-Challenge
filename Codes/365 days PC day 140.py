#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:41:16 2023

@author: boladipo
"""





## Convert a Decimal number to a Roman Numeral using Python



decimal_num = int(input("Enter a Decimla Number : "))







def decimal_to_roma(decimal_num):
    roman_to_decimal_dict = {1000 : "M", 900 : "CM", 500 : "D", 400: "CD",
                             100 : "C", 90 : "XC", 50 : "L", 40 : "XL", 10: "X",
                             9:"IX", 5 : "V", 4 : "IV", 1: "I"}
    
    
    roman_numeral = ''
    
    for value, numeral in roman_to_decimal_dict.items():
        while decimal_num >= value:
            roman_numeral += numeral
            decimal_num  -= value
    return roman_numeral
print(decimal_to_roma(decimal_num))