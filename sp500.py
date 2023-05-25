import bs4 as bs
import requests
import pickle
import os 
import datetime as dt
import pandas_datareader as web

def load_sp500_tickers():

    link = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    # print(link.text)
    soup = bs.BeautifulSoup(link.text)
    
    tickers = []
    table = soup.find('table', {'id' : 'constituents'})
    # print(table.text)
    rows = table.findAll('tr')[1:]
        
    for row in rows:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker[:-1])

    # print(tickers)

    #serializing the ticker object
    with open('snp500.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    
    with open('snp500.pickle', 'rb') as f:
        tickers = pickle.load(f)
    
    print(tickers)


# load_sp500_tickers()


# def load_prices(reload_tickers = False ):
#     if reload_tickers:
#         tickers = load_sp500_tickers()
#     else:
#         if os.path.exists('sp500tickers.pickle'):
#             with open ('sp500tickers.pickle','rb') as f:
#                 tickers = pickle.load(f)
#         if not os.path.exists('companies'):
#             os.makedirs('companies')


# start = dt.time(2018, 1, 1)
# end = dt.time(2022, 1, 1)

# for ticker in tickers:
#     if not os.path.exists('companies/{}.csv'.format(ticker))

