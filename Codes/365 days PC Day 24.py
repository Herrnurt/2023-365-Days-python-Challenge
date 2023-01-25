#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:52:29 2023

@author: boladipo
"""

## Validate NAgrams using Python




def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)




print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))
print(anagram("python", "python"))