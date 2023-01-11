#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:42:08 2023

@author: boladipo
"""

## Text to Handwriting using Python

import pywhatkit as kit
import cv2


Handwritten = input("Enter your text to convert in Handwriting : ")
kit.text_to_handwriting(Handwritten, save_to = "pythoncoding.png")
img = cv2.imread("pythoncoding.png")

cv2.imshow("Python Coding", img)
cv2.waitkey(0)
cv2.destroyAllWindows()
