#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:42:33 2023

@author: boladipo
"""



## Programm ro find edges of a coins




# The skimage comes with data built-in that you can run computer vision on


from skimage import data, io, filters

image = data.coins()


edges = filters.sobel(image)
#edges = filters._gaussian(image)
io.imshow(edges)
