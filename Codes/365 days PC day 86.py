#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:46:13 2023

@author: boladipo
"""



### WebBrowser in Python




import webbrowser


Url = input("Enter a url :")
webbrowser.open(Url)




# Open the page in a new browser window

webbrowser.open_new("Url")






# Open the page in a new broswer tab
webbrowser.open_new_tab("Url")