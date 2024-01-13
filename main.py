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
    '''
    Line 17 is declaring a varaible called hist. This is going to grab 
    the historical market data over the last 10 days.
    '''
    hist = stock.history(period="10d")

    '''
    Empty list that will be used later in the program.
    '''
    closingList = []


    '''
    This for loop is going to go through the history of the selected stocks
    and find the closing price for each of them. Then it will add those prices 
    to the closinglist and round the price by 2 decimals.
    '''
    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList



stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

msftClosing = np.array(getClosing("MSFT"))
days = list(range(1, len(msftClosing) + 1))

plt.plot(days, msftClosing)

prices = getClosing("MSFT")
prices.sort()
low_price = prices[0]
high_price = prices[-1]

plt.axis([1,10,low_price,high_price])


plt.ylabel("Closing Price")
plt.xlabel("Days")
plt.title("Closing price for " + "MSFT")
plt.show()
