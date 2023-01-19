#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:20:53 2023

@author: boladipo
"""



# Three-Dimentional contour plots


import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(np.sqrt(x **2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

x, y = np.meshgrid(x,y)
z = f(x, y)

fig = plt.figure()
ax= plt.axes(projection = '3d')
ax.contour3D(x, y,z, 60, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()