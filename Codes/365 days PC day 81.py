#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:42:57 2023

@author: boladipo
"""

# URL Shortener with Python



import pyshorteners

long_url = input("Ente the URL to shorten")


type_tiny = pyshorteners.Shorteners()
short_url = type_tiny.tinyurl.short(long_url)



print("The shortened URL is: " + short_url)