#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:58:30 2023

@author: boladipo
"""



#  Selection OSrt in Python


def selectionSort(List):
    for i in range (len(List) - 1):  # for iterating n-1 times
        minimum = i
        for j in range(i + 1, len(List)): # Compare i and i +1 element
            if (List[j] < List[minimum]):
                minimum = j
                
            if (minimum  != i):
                List[i], List[minimum] = List[minimum], List[i]
                
        return List
    
    
if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9, 8]
    
    print('Sorted List:', selectionSort(List))

        