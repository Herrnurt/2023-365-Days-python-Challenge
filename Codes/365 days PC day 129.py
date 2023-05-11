#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:39:23 2023

@author: boladipo
"""

### Country Details using Python


from countryinfo import CountryInfo

count = input("Enter your country :")

country = CountryInfo(count)

print("Capital is :", country.capital())
print("Currencies is :", country.currencies())
print("Language is :", country.languages())
print("Borders are :", country.borders())
print("Others names :", country.alt_spellings())

