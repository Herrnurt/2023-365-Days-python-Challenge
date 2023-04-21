#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:43:17 2023

@author: boladipo
"""







# Pdf to Audio using Python



import PyPDF2, pyttsx3




# PDF file

path = open('pdf.pdf', 'rb')




# created a pdffileReader object

pdfReader = PyPDF2.PdfFileReader(path)



# Get an engine instance for the speech synthesis 

speak = pyttsx3.init()



for pages in range(pdfReader.numPages):
    text = pdfReader.getpage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
    
speak.stop()