#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:42:48 2023

@author: boladipo
"""



## Generate Barcode using Python



import barcode
from barcode.writer import ImageWriter






# define content of the barcode as a string
number = input("Enter the code to generater barcode : ")



# get the required barcode format
barcode_format = barcode.get_barcode_class('upc')


# genearte barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())



#Save barcode as PNG

my_barcode.save("generated_barcoode")


