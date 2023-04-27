#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:55:04 2023

@author: boladipo
"""



## Create Beautiful Graphs

import plotly.express as plotly
import plotly.graph_objects as graph


# Draw Bar Chart
plot = plotly.bar(x=['D1', 'D2', 'D3'], y =[1, 2, 3])
plot.show()



# Draw Scatter Chart 
plot = plotly.scatter(x=[1, 2,3,], y =[1, 2, 3])
plot.show()


# Draw Pie Chart
plot = plotly.pie(labels=['D1', 'D2', 'D3'], values =[1, 2, 3])
plot.show()

## Draw Histogram
plot = plotly.histogram(x=[1, 2, 3])
plot.show()


#Draw Box plot

plot = plotly.box(x=[1, 2, 3])
plot.show()

