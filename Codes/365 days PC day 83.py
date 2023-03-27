#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 23:38:55 2023

@author: boladipo
"""
## Convert PDF to docx using Python



from pdf2docx import Converter

pdf_file = 'bolaji.pdf'
docx_file = 'sample.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)

cv.close()