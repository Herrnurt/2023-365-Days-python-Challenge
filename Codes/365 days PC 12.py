#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:05:33 2023

@author: boladipo
"""

## Language Detection using Python


from langdetect import detect

text = input("Enter any text in any language :")
print(detect(text))