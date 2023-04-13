#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:43:01 2023

@author: boladipo
"""






import pandas as pd

import csv,json


data = pd.read_csv("Instagram.csv")

print(data)

print("Converted JSON file below")
print(json.dumps(list(csv.reader(open("Instagram.csv")))))