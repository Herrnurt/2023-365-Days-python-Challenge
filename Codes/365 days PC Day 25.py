#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:02:03 2023

@author: boladipo
"""

## Extracting Text from PDF with python


import PyPDF2


pdf = open("pythonclcoding.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())


