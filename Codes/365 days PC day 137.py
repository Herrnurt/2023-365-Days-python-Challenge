#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 23:44:47 2023

@author: boladipo
"""




### Python Program for WordClouds



from wordcloud import wordCloud
import matplotlib.pyplot as plt





# open the text file


with open('Clcoding.txt', 'r') as f:
    text = f.read()
    
    
    
# Generate the word cloud
wordcloud = wordCloud().generate(text)
                      
                      
# Display the word cloud
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()