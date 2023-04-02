#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 23:07:36 2023

@author: boladipo
"""





## Image Mirroe with Python

from PIL import Image


Image.open('binodd.jpg')  #original Image



img = Image.open('binodd.jpg')

Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r"blood_mirror.png")


Image.open("binod_mirroe.png")