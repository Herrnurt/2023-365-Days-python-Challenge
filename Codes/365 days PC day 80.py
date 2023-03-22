#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:40:05 2023

@author: boladipo
"""

# pip install PyPDF2
# pip install pyttsx3


# Create an AUdio Book in Python
import PyPDF2
import pyttsx3

# Read the pdf by specifying the path in your computer
pdfReader = PyPDF2.PdfFileReader(open("file.pdf", 'rb'))


# Get the handle to speaker
speaker = pyttsx3.init()

# Split the pages and read one by one

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extratText()
    
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
    
#stop the speaker after completion
speaker.stop()
# save the audiobook at specified path
engine.save_to_file(text, "path/file.mp3")
engine.runAndWait()