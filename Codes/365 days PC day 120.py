#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:42:36 2023

@author: boladipo
"""




# Remove Image background using Python


from rembg import remove

from PIL import Image

input_path = 'image.png'

output_path = 'output.png'

input = Image.open(input_path)

output = remove(input)

output.save(output_path)
