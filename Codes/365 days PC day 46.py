#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:44:05 2023

@author: boladipo
"""

## Get Zip Code with given location using GeoPy in Python


from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent = "geoapiExercises")



place = input("enter City Name: ")
location = geolocator.geocode(place)
print(location)