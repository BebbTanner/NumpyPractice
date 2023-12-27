import yfinance as yf
import pprint

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period = "10d")
    closingList = []
    for price in hist['Close']:
        closingList.append(price)

    return closingList



msft = getClosing('MSFT')

pprint.pprint(msft)

