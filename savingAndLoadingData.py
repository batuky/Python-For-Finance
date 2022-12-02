from pandas_datareader import data as web
import datetime as dt
import pandas as pd
import codecs

#chapter 1-2

#Loading data
start = dt.datetime(2019,1,1)
end = dt.datetime.now()

df = web.DataReader( 'AAPL' , 'yahoo' , start, end)

#print(df)


#Reading individual values
#it is printing just closing values
# print(df['Close'])

#it is giving daily value.
# print(df['Close']['2022-02-14'])

#it is showing fifth data
# print (df[ 'Close' ][ 5 ])


#saving and loading data 

df.to_html( 'apple.html' )

#control that func. find another alternative to read the html file
df = pd.read_html( "apple.html")
print(df)

# fk nın ingilizcesini bul fk rate i hesapla. 
