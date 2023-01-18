#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:38:49 2023

@author: boladipo
"""

## Age Calculator using Python


def ageCalculator(year, month, day):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, day)
    age = int((today-dob).days/ 365.25)
    print(today)
    print(dob)
    print(age)



ageCalculator(1986, 11, 27)