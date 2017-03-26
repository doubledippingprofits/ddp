#imports
import datetime
import pandas as pd
import numpy as np
import pandas_datareader.data as data
import os
#froms
from pandas import Series, expanding_mean, expanding_std, ewma, ewmstd, show_versions, DataFrame
from datetime import timedelta
ewm = pd.DataFrame.ewm

#remove raw_data.csv
os.remove("raw_data.csv")
print("File Removed!")

#read csv file and set symbols_list array to csv symbols
symbols = pd.read_csv('symbol_list.csv',delimiter="\t")
symbols_list = []
for symbol in symbols['Symbol']:
    symbols_list.append(symbol)

#set start and end date to pull stock data
start = datetime.datetime.today() - timedelta(days=400)
end = datetime.datetime.today()


symbols=[]

for ticker in symbols_list:	
	span_eight = 8
	span_thirtyfour = 34
	r = data.DataReader(ticker,'yahoo',start,end)
	
	rest_eight = r['Close'][span_eight:]
	rest_thirtyfour = r['Close'][span_thirtyfour:]
	
	#add '8MA' to output to see
	r['8MA'] = r['Close'].rolling(window=8, min_periods=8).mean()[:span_eight]
	r['8EMA'] = rest_eight.ewm(span=span_eight, adjust=False).mean()
	
	r['20MA'] = r['Close'].rolling(window=20, min_periods=20).mean()
	
	#add '34MA' to output to see
	r['34MA'] = r['Close'].rolling(window=34).mean()[:span_thirtyfour]
	r['34EMA'] = rest_thirtyfour.ewm(span=span_thirtyfour, adjust=False).mean()

	#r['50MA'] = r['Close'].rolling(window=50, min_periods=50).mean()
	#r['200MA'] = r['Close'].rolling(window=200, min_periods=200).mean()
	
	r['GREEN'] = (r['Close']-r['Open'])>0
	
	#r['BOBO'] = ((r['34EMA'] > r['20MA'])&(r['20MA'] > r['Close'])&(r['Close'] > r['8EMA'])&(r['GREEN'] == True))

	r['BOBO'] = (r['GREEN'] == True)&(r['Close'] > r['8EMA'])&(r['Close'] < r['20MA'])&(r['Open'] < r['8EMA'])&(r['Close'] < r['34EMA'])
	
	
	
	
	#(r['Open'] < r['8EMA'])&(r['Close'] > r['8EMA'])&(r['34EMA'] > r['20MA'])&(r['GREEN'] == True)
	
	# add a symbol column
	r['Symbol'] = ticker
	
	symbols.append(r)
	
# concatenate all the dfs
df = pd.concat(symbols)

print symbols

#define cell with the columns that i need
# NOTE!!!!: REMOVED 'Volume' , re-add to see in csv
cell= df[['Symbol','Open','High','Low','Close','8EMA','20MA','34EMA','GREEN','BOBO']]

#changing sort of Symbol (ascending) and Date(descending) setting Symbol as first column and changing date format
cell.reset_index().sort(['Symbol', 'Date'], ascending=[1,1]).set_index('Symbol').to_csv('raw_data.csv', date_format='%d/%m/%Y')