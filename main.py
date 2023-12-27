import yfinance as yf
import pprint


'''
Created a variable called msft. This is going to go out to 
yahoo finance and grab the ticker information for microsoft.
'''
msft = yf.Ticker("MSFT")

# get historical market data
hist = msft.history(period="10d")

'''
For loop that is going through all of the information in
the hist variable and finding the values labeled close.
It is then printing out those values.
'''
for price in hist['Close']:
    pprint.pprint(price)

