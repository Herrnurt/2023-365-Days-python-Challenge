#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:58:04 2023

@author: boladipo
"""

# Text Wrapping in Python




import textwrap



value = """ this function wraps the input paragraph such that each line in the \
    paragraph is at most width characters long. The wrap method returns a list of output lines.\
        The returned list output has no content"""


# wrap this text
wrapper = textwrap.TextWrapper(width = 60)


word_list = wrapper.wrap(text=value)



# print each line.


for element in word_list:
    print(element)
    
    
    