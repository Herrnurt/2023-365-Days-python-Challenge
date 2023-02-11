#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:36:15 2023

@author: boladipo
"""


## Image to Pencil Sketch in Python


import cv2


# specify the path to image (landing image image)
image1 = cv2.imread('/Users/boladipo/Downloads/pythonlogo.png')
window_name = "Original image"

# displaying the Original image
cv2.imshow(window_name, image1)


# Convert the image from one color space to another
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)


# image smoothing

blur = cv2.GaussianBlur(invert, (21,21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale =256.0)

# save the converted image to specified path
cv2.imwrite("E:\sketch.png", sketch)


# reading an image in default mode
image = cv2.imread("E:\sketch.png")


# Displaying the sketch image
cv2.imshow(window_name, image)

# write for user to press any key
# (this is the necessary to avoid python kernel form crashing)
cv2.waitkey(0)


# closing all open windows

cv2.destroyAllwindows()