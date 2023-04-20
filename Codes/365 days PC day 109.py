#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:36:29 2023

@author: boladipo
"""



## Find ALL Python Errors




import re

for i in dir(__builtins__):
    if re.match(r'^[A-Z]', i):
        print(i)