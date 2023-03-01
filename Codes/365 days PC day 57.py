#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:44:24 2023

@author: boladipo
"""

## Number Guessing Game




import random
import math


lower = int(input("Enter Lower bound:- "))
upper = int(input('Enter Upper bound:_ '))

# genertaing random number between the lower and upper

x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

 # initializing the number of guesses.
count = 0
      
# for calculation of minimun number of guesses depends upon range
      
while count < math.log(upper - lower + 1, 2):
    count += 1
          
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",count, "try")
        break
    elif x > guess:
        print("you guesssed too small")
    elif x < guess:
        print("you Guessed too high")
              
# shows this output
    
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck Next time")
