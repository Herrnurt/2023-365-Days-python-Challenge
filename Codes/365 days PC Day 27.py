#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:07:59 2023

@author: boladipo
"""



## Pie charts using Matplotlib in Python


import matplotlib.pyplot as plt

labels = ("python", "Java", "Scala", "C#")
sizes = [45, 30, 15, 10]

plt.pie(sizes, labels=labels, autopct='%1.f%%', counterclock = False, 
        startangle=105)


plt.show()