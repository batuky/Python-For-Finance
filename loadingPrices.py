import os 
import datetime as dt
import pandas_datareader as web
from sp500 import load_sp500_tickers


def load_prices(reload_tickers = False ):
    if reload_tickers:
        tickers = load_sp500_tickers()
    else:
        if os.path.exists('sp500tickers.pickle'):
            with open ('sp500tickers.pickle','rb') as f:
                tickers = pickle.load(f)
        if not os.path.exists('companies'):
            os.makedirs('companies')


start = dt.time(2016, 1, 1)
end = dt.time(2019, 1, 1)

# for ticker in tickers:
#     if n