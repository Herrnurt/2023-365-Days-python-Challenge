#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:41:40 2023

@author: boladipo
"""


## Empyty Recycle Bin using Python




import winshell


try:
    winshell.recycle_bin().empty(comfirm=False, show_progress=False, sound=True)
    
    
    print("Recycle bin emptied Now")
    
    
except:
    
    
    print("Recycle bin already empty")
    