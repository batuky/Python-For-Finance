import bs4 as bs
import requests
import pickle

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

    with open('snp500.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    
    with open('snp500.pickle', 'rb') as f:
        tickers = pickle.load(f)
    
    print(tickers)


load_sp500_tickers()


