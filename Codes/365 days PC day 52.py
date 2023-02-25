#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:09:52 2023

@author: boladipo
"""

## Prlimes smaller than or equl to the Number


def primesNumber(n):
    primes = [True] * (n +1)
    
    p = 2       # because p is the smallest prime
    while (p * p <= n):
        
        # if p is not marked as False, this it is a prime
        
        if (primes[p]) == True:
            # mark all multiples of number as False
            for i in range(p * 2, n + 1, p):
                primes[i] = False
                
                
        p += 1
        
        # printing all primes
        
    for i in range(2, n):
        if primes[i]:
            print(i)
                
                
if __name__ == '__main__':
    n = int(input("enter a no to check all smaller prime numbers :"))
    primesNumber(n)
