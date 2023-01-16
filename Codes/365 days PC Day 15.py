#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:13:51 2023

@author: boladipo
"""
# Violin plot using Python



import seaborn as sns
import matplotlib.pyplot as plt


data = sns.load_dataset("tips")

plt.figure(figsize = (10, 4))

sns.violinplot(x=data["total_bill"])
plt.show()