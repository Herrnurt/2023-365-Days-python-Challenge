#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:27:28 2023

@author: boladipo
"""

### A Music player in python




import pygame
import tkinter as tk
from tkinter import filedialog
def play_music():
    
    # open a file dialong to slect the music file
    filename = filedialog.askopenfilename()
    pygame.init()
    pygame.mixer.init()
    pygame.ixer.music.load(filename)
    pygame.mixer.music.play()
    
    
    
    
# Create a GUI using tkinter
root = tk.TK()
root.title("Musci Player")

play_button = tk.Button(root, text= "Play", command = play_music)
play_button.pack()
root.mainloop()