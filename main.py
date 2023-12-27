import yfinance as yf
import pprint


'''
Created a variable called msft. This is going to go out to 
yahoo finance and grab the ticker information for microsoft.
'''
msft = yf.Ticker("MSFT")

# get all stock info
pprint.pprint(msft.info)
