#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:41:46 2023

@author: boladipo
"""




## Fetch PDF Text in python



import pdfplumber as pdftool


def Fetch_Text(file_path):
    
    # extract page by page
    
    with pdftool.open(file_path) as tool:
        for p_no, page in enumerate(tool.pages, 1):
            print('<--- page no', p_no, '---')
            
            data = page.extract_text()
            
            print(data)
            
            
Fetch_Text('NIW.pdf')