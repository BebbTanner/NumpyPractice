import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint

'''
Function that is setup to grab stock information for 
whatever stock is kicked into it. For now the stocks 
selected are hard coded in, but I would like to add a
feature where the user selects those 5 stocks.
'''
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
