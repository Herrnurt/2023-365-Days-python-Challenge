#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:03:51 2023

@author: boladipo
"""



## Rangoli Paanteern using Alphabets

def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    
    data = [alpha[i] for i in range(size)]
    
    items = list(range(size))
    
    items = items[:-1] + items[::-1]
    
    
    for i in items:
        temp = data[-(i+1):]
        
        row = temp[::-1] + temp[1:]
        
        print(",".join(row).center(n*4-3, "."))
        
        
if __name__ == '__main__':
    n = int(input())
    
    print_rangoli(n)