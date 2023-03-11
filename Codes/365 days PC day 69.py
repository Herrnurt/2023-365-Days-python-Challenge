#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:35:39 2023

@author: boladipo
"""

## Permutations of a given string




from itertools import permutations
def allPermutations(str):
    
    
    
    
    # Get all permutations of string 'ABC'


    permList = permutations(str)
    
    
    
    
    
    
    # print all permutation
    
    for perm in list(permList):
        print(''.join(perm))
        
        
        
        
# Driver program


if __name__ == "__main--":
    str = input("Enetr your string : ")
    allPermutations(str)