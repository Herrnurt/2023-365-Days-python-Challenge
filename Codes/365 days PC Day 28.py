#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:54:52 2023

@author: boladipo
"""



## Bar Grapgh using Matplotlib in Python

import matplotlib.pyplot as plt



# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5, ) # provide locations on x axis
sizes = [45, 10, 15, 30, 22]

# Set up the bar chart

plt.bar(index, sizes, tick_label = labels)


# Configure the layout
plt.ylabel('USage')
plt.xlabel("Programming Language")

# Diplay the chart
plt.show()
