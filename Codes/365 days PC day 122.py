#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 23:37:40 2023

@author: boladipo
"""


## Image Compression using python






import PIL
from PIL import Image
from tkinter.filedialog import *


fl = askopenfilenames()
img = Image.open(fl[0])
img.save("co.jpg", "JPEG", optimize = True, quality = 10)


Image.open('co.jpg') 