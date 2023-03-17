#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:01:26 2023

@author: boladipo
"""

# Convert videos files to a gif in python



from mpviepy.editor import VideoFileClip


videoClip = VideoFileClip("Blind.mp4")
videoClip.write_gif("Blind.gif")