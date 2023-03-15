#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:38:10 2023

@author: boladipo
"""



### Gte address detail through python code



from geopy.geocoders import Nominatim




# Using Nominatim APi
geolocator = Nominatim(user_agent = "geoapiExercises")



# Zipcode input

a = input("Enter the zipcode : ")

zipcode = a

# Using geocode()

location = geolocator.geocode(zipcode)



# displaying address details
print("Zipcode: ", zipcode)
print("Details of the Zipcode")
print(location)
