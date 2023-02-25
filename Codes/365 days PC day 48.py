#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:26:06 2023

@author: boladipo
"""

## Bubble Sort using python


def bubbleSort(List):
    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]
                
                
    return List



if __name__ =='__main__':
    List = [8, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:', bubbleSort(List))