#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:28:49 2023

@author: boladipo
"""

 


#  Program to cteate a Countdown Timer



import time
 

def countdown(time_sec):
    
    while time_sec:
        mins, secs = divmod(time_sec , 60)
        timeformat = '{:02d}: {:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        
        
    print('stop')
    
num = int(input("Set Your Timer :"))
countdown(num)