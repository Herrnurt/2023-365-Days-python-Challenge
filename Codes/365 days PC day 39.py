#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:19:45 2023

@author: boladipo
"""

## QR Code using Python

import pyqrcode


link = "https://www.instagram.com/pythonclcoding/"
qr_code = pyqrcode.create(link)
qr_code.png("Instagram.png", scale = 5)


## Decode a QR Code using Python

from pyzbar.pyzbar import decode

from PIL import Image

decocdeQR = decode(Image.open('instagram1.png'))
print(decocdeQR[0].data.decode(ascii))