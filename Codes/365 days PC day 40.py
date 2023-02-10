#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:42:06 2023

@author: boladipo
"""

## Excution Time of a Python Program

from time import time


start = time()


# Count Start
email = input("Enter Your Email: ")
email = email.strip()


slicer_index = email.index("@")
username = email[:slicer_index]
domain_name = email[slicer_index + 1:]


print("Your user name is ", username, "and your domain is ", domain_name)

# code end



end = time()
execution_time = end -start
print('Execution Time (s) :', execution_time)


