#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:30:54 2023

@author: boladipo
"""



## Convert png to jpeg duing python



from Pil import Image

im = Image.open('clcodingpng.png')

rgb_im = im.converts('RGB')
rgb_im.save('clcodingpng.jpg')