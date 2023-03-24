#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:33:19 2023

@author: boladipo
"""



## Unzip File Using Python

from zipfile import ZipFile

with ZipFile("binod.zip", 'r') as zip_object:
    zip_object.extractall()
    
    
#List of files that are archived in the ZIP file


print(zip_object.namelist())