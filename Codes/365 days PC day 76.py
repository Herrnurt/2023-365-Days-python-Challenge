#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:35:56 2023

@author: boladipo
"""

## Generate Image captcha in python

from captcha.image import ImageCaptcha

# Specify the image size
image = ImageCaptcha(width = 300, height = 100)


# Specify the Text for captcha
captcha_text = input("Enter Captcha text : ")

# generate the image of th egiven text
data = image.generate(captcha_text)

# write the image on the given file and save it
image.write(captcha_text, '/Users/boladipo/Desktop/CAPTCHA1.png')

from PIL import image

image.open('/Users/boladipo/Desktop/CAPTCHA1.png')
