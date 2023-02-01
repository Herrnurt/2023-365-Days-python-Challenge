#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:12:00 2023

@author: boladipo
"""


## Radar Plot using Python

import plotly.express as px

import pandas as pd

data = pd.DataFrame(dict(keys = [10, 20, 30, 40], values = ["Labousr Cost", "Manufacturing cost", 
                                                            "Promotion Cost", "Selling cost"]))


figure = px. line_polar(data, r = 'keys', theta ='values', line_close=True)
figure.show()