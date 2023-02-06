#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:44:50 2023

@author: boladipo
"""


## Remove Cuss words using Python



from better_profanity import profanity

text = input("ENter your sentence to check :")
censored = profanity.censor(text)
print(censored)