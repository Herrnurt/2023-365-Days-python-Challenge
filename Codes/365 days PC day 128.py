#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:40:58 2023

@author: boladipo
"""



## Cloud file Sharing using Python




# File Storage
import gofile as go

def Store_Files(file):
    cur_server = go.getServer()
    print(cur_server)
    
    url = go.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
    
Store_Files("new,jpg")