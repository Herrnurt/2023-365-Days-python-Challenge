#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:39:48 2023

@author: boladipo
"""




## Image Watermarking with Python


from PIL import Image, ImageDraw, ImageFont

img = Image.open(r'/Users/boladipo/Desktop/365\Days\Python\Challege/African_Bush_Elephant.jpeg')
draw = ImageDraw.Draw(img)

text = "Bolaji Oladipo"

font = ImageFont.truetype('arial.ttf', 50)
textwidth, textheight = draw.textsize(text, font)
width, height = img.size
x = ((width/2)-(textwidth/2)) 
y = height-textheight -50

draw.ext((x, y), text, font = font)
img.save(r'elephant.png')
Image.open('elephant.png')