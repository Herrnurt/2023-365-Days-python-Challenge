#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:14:20 2023

@author: boladipo
"""

## Calculator in Python


# prompt the user to enter any number


FirstOperand = input("Enter First Operand (Any Numeric value)\n")


# convert entered value to int

FirstOperand = int(FirstOperand)



# Prompt the user to enter any operator


Operator = input("Enter Operator (+, -, *, /, %, //, **)\n")


SecondOperand = input( "Enter Second Operand (Any Numeriv value)\n")

SecondOperand = int(SecondOperand)




# Calculate Answer base on enetred operator

if (Operator == "+"):
    Answer = FirstOperand + SecondOperand
    
if (Operator == "-"):
    Answer = FirstOperand - SecondOperand
    
if (Operator == "*"):
    Answer = FirstOperand * SecondOperand

if (Operator == "/"):
    Answer = FirstOperand / SecondOperand
    
if (Operator == "%"):
    Answer = FirstOperand % SecondOperand

if (Operator == "//"):
    Answer = FirstOperand + SecondOperand
    
if (Operator == "**"):
    Answer = FirstOperand + SecondOperand
    
    
print("Answer = ", Answer)
    
    