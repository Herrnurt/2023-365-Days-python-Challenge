#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:08:17 2023

@author: boladipo
"""

## Insertion Sort Using Python



def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        for j in range(i-1, -1, -1):
            if List[j] > currentNumber:
                List[j], List[j +1] = List[j +1], List[j]
            else:
                List[j + 1] = currentNumber
                
                break
            
    return List


if __name__ == '__main__':
    List = [5, 2, 4, 6, 8, 7, 1]
    print("SOrted List:", insertionSort(List))