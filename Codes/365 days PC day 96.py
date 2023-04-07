#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:41:19 2023

@author: boladipo
"""

## Track phone number using Python



import phonenumbers


# import geocoder

from phonenumbers import geocoder



# specify then phone number
a = input("Enter the Phone Number: ")

phonenumber = phonenumbers.parse(a)


# displat the location of phone number

print(geocoder.description_for_number(phonenumber, 'en'))