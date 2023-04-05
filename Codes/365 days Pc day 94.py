#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:51:50 2023

@author: boladipo
"""



## extract Text from Image Using Python


from PIL import Image
from pytesseract import pytesseract


# Define apth to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image

path_to_image = 'texttoimage.png'



# Point tessaract_cmd to tessract.exe
pytesseract.tesseract_cmd = path_to_tesseract



# open image with PIL
img = Image.open(path_to_image)


# Extract text from image
text = pytesseract.image_to_string(img)


print(text)