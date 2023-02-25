#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:45:16 2023

@author: boladipo
"""

## Count number of files and directories


import os


# Pathe in which we have to count files and directories

PATH = 'E:\desktop'     # Give your path here

fileCount =0
dirCount = 0


for root, dirs, files in os.walk(PATH):
    print('Looking in :', root)
    for directories in dirs:
        dirCount += 1
        
    for Files in files:
        fileCount += 1
        



print("Number of files", fileCount)
print('Number of Directories', dirCount)
print("Total:", dirCount + fileCount)