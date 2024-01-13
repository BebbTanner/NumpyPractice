'''
Closing stock price program

This program will ask the user to enter 5 stock tickers. It will then
get the closing price of those stocks for the last 10 days and save them as arrays.
It will then convert that into a line graph and save them as PNG's in the Charts folder.
'''


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint
import copy

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


stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing) + 1))

    plt.plot(days, stockClosing)

    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    plt.axis([1,10,low_price - 5,high_price + 5])

    plt.ylabel("Closing Price")
    plt.xlabel("Days")
    plt.title("Closing price for " + stock)

    saveFile = "Charts/" + stock + ".png"
    plt.savefig(saveFile)

    plt.show()

