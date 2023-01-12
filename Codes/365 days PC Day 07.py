#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:17:45 2023

@author: boladipo
"""


import plotly.graph_objects as go


fig = go.Figure(go.Treemap(
    
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"] ))


fig.show()
