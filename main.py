import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")
    closingList = []
    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList


'''
Stocks list that has the 5 stocks selected
'''
stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

stockArray = np.array(stocks)
