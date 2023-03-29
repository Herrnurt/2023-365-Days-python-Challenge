#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:46:00 2023

@author: boladipo
"""



## Download PDF books from internet


import urllib.request


url = input("Enter link to Download PDF : ")

Name = input("Enter a Name for the PDF File : ")

FileName = Name +".pdf"

urllib.request.urlretrieve(url, FileName)