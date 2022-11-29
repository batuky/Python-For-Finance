from pandas_datareader import data as web
import datetime as dt

#get data from yahoo api
start = dt.datetime[2019,1,1]
end = dt.datetime.now()

df = web.DataReader( 'AAPL' , 'yahoo' , start, end)