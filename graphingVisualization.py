from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

# Chapter 3
# #get data from yahoo api
# start = dt.datetime(2019,1,1)
# end = dt.datetime.now()

# # df = web.DataReader( 'AAPL' , 'yahoo' , start, end)
# apple = web.DataReader( 'AAPL' , 'yahoo' , start, end)
# apple[ 'Adj Close' ].plot(label = "AAPL")
# #plotting diagram
# # df[ 'Adj Close' ].plot()
# # plt.show()

# #plotting style
# style.use('ggplot')
# plt.ylabel('adjusted close')
# plt.title('AAPL share price')
# #On the left corner, it is showing colors with share names
# plt.legend( loc = 'upper left' )
# plt.show()


#Comparing stocks

# style.use('ggplot')
# start = dt.datetime(2021,1,1)
# end = dt.datetime(2022,10,1)
# apple = web.DataReader('AAPL', 'yahoo', start, end) 
# facebook = web.DataReader('FB', 'yahoo', start, end) 

# apple['Adj Close'].plot(label= 'AAPL')
# facebook['Adj Close'].plot(label= 'FB')

# plt.ylabel('Adjusted Close')
# plt.legend(loc= 'upper left')
# plt.show()


#Comparing stocks with sub plots

style.use('ggplot')
start = dt.datetime(2020,1,1)
end = dt.datetime(2022,10,1)
apple = web.DataReader('AAPL', 'yahoo', start, end)
amazon = web.DataReader('AMZN', 'yahoo', start, end)

plt.subplot(211)
apple['Adj Close'].plot(label= 'AAPL', color = 'blue' )
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price')

plt.subplot(212)
amazon['Adj Close'].plot(label= 'AMZN', color = 'red' )
plt.ylabel('Adjusted Close')
plt.title('AMZN Share Price')

plt.tight_layout() #When I dont use the func, graphs are mixing
plt.show()

