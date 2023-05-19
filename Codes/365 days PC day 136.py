#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:32:06 2023

@author: boladipo
"""




## Language Detection using Python

import langid
def detect_language(text):
    return langid.classify(text)[0]
    
    
text = input("Enter in any Language :")
print(detect_language(text))