#!/usr/bin/env python
# coding=utf-8

prices = {
    'ACME': 45.23,    
    'AAPL': 612.78,    
    'IBM': 205.55,    
    'HPQ': 37.20,    
    'FB': 10.75  
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = min(zip(prices.values(), prices.keys()))

    