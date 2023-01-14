#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:01:48 2023

@author: boladipo
"""

# CountryInfo in Python


from countryinfo import CountryInfo
count = input("Enter your country :")


country =CountryInfo(count)
print("Capital is : ", country.capital())
print("FLag is : ", country.flag())
print("Area is : ", country.area())
print("Calling codes is : ", country.calling_codes())
print("Population is : ", country.population())
print("Demonyn is : ", country.demonym())
print("Currencies is :", country.currencies())
print("Province are : ", country.provinces())
print("Region is : ", country.region())
print("Language is : ", country.languages())
print("TIme Zone is : ", country.timezones())
print("Lattidude and Logitude are : ", country.latlng())
print("Borders are : ", country.borders())
print("Others names : ", country.alt_spellings())