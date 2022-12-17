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

apple[ '100d_ma' ] = apple[ 'Adj Close' ].rolling( window = 100 , min_periods = 0 ).mean()
apple[ 'PCT_Change' ] = (apple[ 'Close' ] - apple[ 'Open' ]) / apple[ 'Open' ]
apple[ 'HL_PCT' ] = (apple[ 'High' ] - apple[ 'Low' ]) / apple[ 'Close' ]

apple.dropna( inplace = True )
print (apple.head())

ax1 = plt.subplot2grid(( 6 , 1 ),( 0 , 0 ), rowspan = 4 , colspan = 1 )
ax2 = plt.subplot2grid(( 6 , 1 ),( 4 , 0 ), rowspan = 2 , colspan = 1 , sharex =ax1)



ax1.plot(apple.index, apple[ 'Adj Close' ], color = 'blue', label = 'Adj Close')
ax1.plot(apple.index, apple[ '100d_ma' ], color = 'orange', label = '100d_ma')
ax2.fill_between(apple.index, apple[ 'Volume' ], color = 'blue', label = 'Volume')
print(apple[ 'PCT_Change' ])
print(apple[ 'HL_PCT' ])
leg = plt.legend(loc='upper left')
plt.show()