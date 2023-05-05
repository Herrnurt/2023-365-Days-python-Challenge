#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 23:34:38 2023

@author: boladipo
"""


## Convert png to jpeg using Python


from PIL import Image



# input Image in png format

im = Image.open("clcodingpng.png")

rgb_im = im.comvert('RGB')



# output Image in jpeg format
rgb_im.save('clcodingpng.jpg')