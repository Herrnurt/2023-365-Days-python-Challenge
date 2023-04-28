#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:40:31 2023

@author: boladipo
"""



# Default mutable arguments



def func(default_arg=[]):
    default_arg.append("python")
    return default_arg


print(func())
print(func())
print(func())