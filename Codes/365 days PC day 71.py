#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 23:40:26 2023

@author: boladipo
"""



# GIF creation in Python



Import imageio

filenames = ["sketch.png", "original.png"]



images = []

for filename in filenames:
    images.append(imageio.imread(filename))
    
imageio.imsave('movie.gif', images, 'GIF', duration =1)
    