#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:33:44 2023

@author: boladipo
"""


## Calculate a hash of a file



import hashlib


BLOCKSIZE = 65536


# Block read size if file is big enough


fileToOpen = '/Users/boladipo/Downloads/PMAR/Project'

hasher = hashlib.md5()

with open(fileToOpen, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
        
print(hasher.hexdigest())