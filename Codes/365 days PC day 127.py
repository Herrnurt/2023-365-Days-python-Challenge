#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:38:42 2023

@author: boladipo
"""





## Get Window Version


# pip install wmi
import wmi


data = wmi.WMI()


for os_name in data.win32_OperatingSystem():
    print(os_name.Caption)