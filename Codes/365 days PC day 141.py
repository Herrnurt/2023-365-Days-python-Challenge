#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:41:33 2023

@author: boladipo
"""




## Python Program for Spider Chart




import matplotlib.pyplot as plt
import numpy as np





# Data 
categories = ['Speed', 'Power', 'Accuracy', 'Endurance', 'Agility']

player1_stats = [90, 75, 85, 80, 90]



# Number of categories

N = len(categories)




# Create an array for the angles
angles = [n / float(N) * 2 * np.pi for n in range(N)]

angles += angles[:1]


# Initialise the plot
fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111, polar=True)



# ADd the first player stats to the plot
stats = player1_stats + player1_stats[:1]
ax.plot(angles, stats, linewidth = 2, linestyle = 'solid', label = 'Player')
ax.fill(angles, stats, alpha = 0.4)




# Set the labels for each axis
ax.set_thetagrids(np.degrees(angles[:-1]), categories)


# Set the range for each axis
ax.set_ylim(0, 100)


# Add a titke
plt.title('Spider chart')



# Add a legend
plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1.1))



# Show the plot
plt.show()