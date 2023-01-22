#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:27:36 2023

@author: boladipo
"""

# Fidget Spinner game with Python


from turtle import *

state = {'turn' : 0}

def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    if state ["turn"] > 0:
        state["turn"] -=1
    spinner()
    ontime(animate, 20)
def flick():
    state["turn"] += 10
    
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()