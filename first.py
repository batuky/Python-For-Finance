from pandas_datareader import data as web
import datetime as dt


start = dt.datetime(2019,1,1)
end = dt.datetime.now()

df = web.DataReader( 'AAPL' , 'yahoo' , start, end)

print(df)

