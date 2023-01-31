#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:16:37 2023

@author: boladipo
"""

import getpass

database = {"clcoding" : "123456", "pythonclcoding": "2502"}
username = input("Enter Your Username : ")
password = getpass.getpass("ENter Your passowrd : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.gtepass("Enter Your Password Again")
            
        break
print("Verified")