#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:23:48 2023

@author: boladipo
"""



## QR Code generation using Python




import pyqrcode
from PIL import Image


link = input("Enter anything to generate QR: ")


qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)

Image.open("QRCode.png")

