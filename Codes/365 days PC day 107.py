#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:42:33 2023

@author: boladipo
"""

## Get Vowels in Python


def get_vowels(String):
    return [each for each in String if each in "aeiou"]

word = input('Enter a word to check Vowels :')
get_vowels(word)