#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 23:19:35 2023

@author: boladipo
"""

import pyautogui


myScreenshot = pyautogui.screenshot()

myScreenshot.save(r"https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png")