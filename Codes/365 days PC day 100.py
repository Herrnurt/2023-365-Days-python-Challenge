#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 23:39:32 2023

@author: boladipo
"""

## Python script that will keep you "online" all day




# import the library pyautogui

import pyautogui

# imports the time library
import time


# run the next lines code while the state is set as "true"


while True:
    # move your cursor 10 pixels
    
    pyautogui.moveRel(0, 10)
    
    # pauses your code from running for 2 seconds
    
    time.sleep(2)