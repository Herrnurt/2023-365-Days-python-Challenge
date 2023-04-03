#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:46:00 2023

@author: boladipo
"""





# detail about Image in Python



from PIL import Image


Image.open('Binodd.jpg')



img = Image.open('Binodd.jpg')
# The file format of the source file

print(img.format) # Output ;JPEG


# The pixel format used by the image
# Typical values are "1", "L", "RGB", or "CMYK"



print(img.mode) # Output ;JPEG
 # Image size, in pixels.
 
 
print(img.size) #Output: (1920, 1280)
 
print(img.palette) #Outpit :None