#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:39:58 2023

@author: boladipo
"""

import random



# range of the values of a dice
min_val = 1
max_val = 6

# to loop the rolling through user input
roll_again = "yes"


# Loop


while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    
    
    # generating and printing 1st random integer from 1 to 6 
    print(random.randint(min_val, max_val))
    
    
    
    # asking user to roll the dice again.
    # Any input order than yes or y will terminate the loop
    roll_again = input("roll the dices again?")
