#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:39:16 2023

@author: boladipo
"""



Height = float(input("Enter your height in centimeters: "))
Weight = float(input("ENter your weight in Kg: "))


Height = Height/100
BMI = Weight/(Height * Height)
print("Your Body Mass Index is: ", BMI)


if (BMI > 0):
    
    if (BMI <= 16):
        print("You are severally underwight")
    elif(BMI <= 18.5):
        print("You are underweight")
    elif(BMI <= 25):
        print("You are Healthy")
    elif(BMI <= 30):
        print("You are Overweight")
    else:
        print("You are severely Overweight")
else:
    ("Enter valid details")
