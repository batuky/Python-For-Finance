from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
#from mpl_finance import candlestick_ohlc this is not working
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates


#Loading data
start = dt.datetime(2019,1,1)
end = dt.datetime.now()

apple = web.DataReader( 'AAPL' , 'yahoo' , start, end)
# #take paramaters.
# apple = apple[[ 'Open' , 'High' , 'Low' , 'Close' ]]

# apple.reset_index( inplace = True )
# apple['Date'] = apple['Date'].map(mdates.date2num)

# print(apple['Date'])
# #creating a plot 
# ax = plt.subplot()
# #managing plot style
# candlestick_ohlc(ax, apple.values, width = 5 , colordown = 'r' , colorup = 'g' )
# ax.grid()
# ax.xaxis_date()
# plt.show()

#take paramaters.
apple = apple[[ 'Open' , 'High' , 'Low' , 'Close', 'Adj Close', 'Volume' ]]


apple_ohlc = apple['Adj Close'].resample( '10D' ).ohlc()
#With date time we can process the data. So with this method we converts our dates in numbers that we can work with
apple_ohlc.reset_index( inplace = True )
apple_ohlc['Date'] = apple_ohlc['Date'].map(mdates.date2num)

apple_volume = apple[ 'Volume' ].resample( '10D' ).sum()

ax1 = plt.subplot2grid(( 6 , 1 ),( 0 , 0 ), rowspan = 4 , colspan = 1 )
ax2 = plt.subplot2grid(( 6 , 1 ),( 4 , 0 ), rowspan = 2 , colspan = 1 , sharex =ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, apple_ohlc.values, width = 5 , colorup= 'g' , colordown = 'r' )

ax2.fill_between(apple_volume.index.map(mdates.date2num), apple_volume.values)
plt.tight_layout()
plt.show()

