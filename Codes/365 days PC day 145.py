#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:41:16 2023

@author: boladipo
"""




## Python Program Color Names to Color Code



from webcolors import name_to_hex


def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    
    except ValueError:
        return None



colorname = input("Enter color name :")


result_code = color_name_to_code(colorname)
print(result_code)
