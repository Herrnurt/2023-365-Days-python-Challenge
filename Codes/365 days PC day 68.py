#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:36:10 2023

@author: boladipo
"""



# Program to find compound interest



def compound_interest(principle, rate, time):
    
    
    #calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    
    CI = Amount - principle
    print("Compound interest is ", CI)
    
    


P = float(input("Enter Principle value : "))
R = float(input("Enter Rate Value : "))

T = float (input("enter Time Value : "))


compound_interest(P,R,T)