#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:40:25 2023

@author: boladipo
"""

## LaTex math description from Python Functions


import math
import latexify



@latexify.with_latex

def solve(a,b,c):
    return (-b + math.sqrt(b**2 -4*a*c)) / (2*(a+b))

solve


@latexify.with_latex
def sinc(x):
    if x == 0:
        return 1
    else: 
        return math.sin(x) / x
sinc



@latexify.with_latex

def greek(alpha, beta, gamma, Omega):
    return alpha * beta + math.gamma(gamma) + Omega
greek