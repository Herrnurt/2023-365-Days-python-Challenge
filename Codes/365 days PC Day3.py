#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:32:33 2023

@author: boladipo
"""

## Palindrome Words using Python


def palindrome (sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")
        
        
    palindrome = []
    words = sentence.split(' ')
    
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
            
    return palindrome
    

sentence = input("Enter a sentense : ")

print(palindrome(sentence))