#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 23:43:26 2023

@author: boladipo
"""



# 5 wyas to remove letters from a string


# 1st method


p = 'clcoding'

p.replace("cl", '')
print(p)


# 2nd method

p = 'clcoding'

p[0:2]
print(p)


# 3rd method

p = 'clcoding'
p.partition('cl')[2]
print(p)

# 4th Method
import re
p = 'clcoding'
re.sub(r'cl', '', p)
print(p)

# 5th Method

p =' clcoding'
p.strip('cl')
print(p)