#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 23:12:17 2023

@author: boladipo
"""

# Line Continuation charaters in Python

print("I Know Python and its very easy for everyone")



# In python, a backslash (\) is a continuation character

print("I know Python abd \
      its very easy for everyone")
      
      
      
      
      
print("I know Python abd \
its very easy for everyone")      




from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("ENter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

print(from_currency, "to", to_currency)

result = c.convert(from_currency, to_currency, amount)
    
print(result)
    
