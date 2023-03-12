#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:29:56 2023

@author: boladipo
"""



## Program to Swap first and Last Element of a List



def swapList(newList):
    size = len(newList)
    
    
    
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size -1]
    newList[size - 1] = temp

    
    
    
    return newList
       
       
       
   
       
     
        


# Driver code

newList = []
 
newList = [int(item) for item in input("enter the list items : ").split()]

print(swapList(newList))