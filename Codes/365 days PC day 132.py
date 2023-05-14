#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:12:57 2023

@author: boladipo
"""








## LIve Exchnage Rates using Python

import urllib3
import json

url = "https://api.exchangerate.host/latest/"
http = urllib3.PoolManager()

response = http.request("GET", url)
data = response.data
currency = json.loads(data)

currency_data = currency['rates']

user = input("Enter a currency :")
for i, j in currency_data.items():
    if i == user:
        print("Current Value = ", j)







