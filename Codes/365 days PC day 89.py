#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:41:21 2023

@author: boladipo
"""



# Get DOmain Name Information Using Python



import whois


domain = input("Enter your Domian : ")
domain_info = whois(domain)

for key, value in domain_info.items():
    print(key, ':', value)
    