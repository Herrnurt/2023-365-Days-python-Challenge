#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:25:42 2023

@author: boladipo
"""

# Progress Bar in python

import sys, time

def progressBar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count/ float(total)))
    
    percent = round(100.0 * count /float(total), 1)
    bar = '=' * filledLength + '-' * (barLength - filledLength)
    
    
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    
    sys.stdout.flush()
    
    
    
    
    for i in range(10):
        time.sleep(1)
        progressBar(i, 10)  