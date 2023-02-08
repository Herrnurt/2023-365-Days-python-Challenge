#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:04:34 2023

@author: boladipo
"""

## Scrape Table from a Website using Python


import urllib.request

import pandas as pd


# List of publicity listed ITES comapnies of india

url =  "https://en.wikipedia.org/wiki/List_of_publicly_listed_software_companies_of_India"



with urllib.request.urlopen(url) as i:
    html = i.read()
    
    
    
    
    
data = pd.read_html(html)[0]
print(data.head())