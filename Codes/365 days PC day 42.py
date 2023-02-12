#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:07:34 2023

@author: boladipo
"""



## Email SLicer in Python



# Ask to enter any email

email = input ("ENter your Email: ")



# Remove any unnecessary white spaces
email = email.strip()


# get the index of @

slicer_index  = email.index("@")


# fetch the user name by string slicing
username = email[:slicer_index]


# fetch the domain name by string slicing
domain_name = email[slicer_index+1:]



# print the result seperatle
print("your user name is ", username, "and your domain is ", domain_name)



