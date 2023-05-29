#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:42:36 2023

@author: boladipo
"""










## Stock Chart Plot using Python




import yfinance as yf


import matplotlib.pyplot as plt



# Doqnload historical data of STOCk

ticker = input("Enter stock Name :")

data = yf.download(ticker, start = "2021-01-01", end = "2023-03-03")


# Plot the stock chart
plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(f"{ticker} Stock Chart")

plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()
