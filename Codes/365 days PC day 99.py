#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:42:36 2023

@author: boladipo
"""

## Word Art From an Image Using Python


from PIL import Image
Image.open("./download.png")

import pywhatkit



pywhatkit.image_to_ascii_art("./download.png", 'MyArt')

# reading text file


read_file = open("MyArt.txt", "r")
print(read_file.read())