#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:43:15 2023

@author: boladipo
"""



## Checking Stocks Using Python




import yfinance as yf

STK = input("Enter share name :")
Share = yf.Ticker(STK).info

market_price = Share["regularMarketPrice"]
print(market_price)