#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:27:03 2023

@author: boladipo
"""




## mages To PDF conversion using Python




from PIL import Image



def Images_Pdf(filename, output):
    images = []
    
    
    for file in filename:
        
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
        
        
        images[0].save(output, save_all=True, append_images=images[1:])
        
# Images path, output pdf
Images_Pdf(["blind-mirror.png", 'binod.png', "binod.jpg"], "output.pdf")