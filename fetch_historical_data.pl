import datetime
import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web
import os

os.remove("raw_data.csv")
print("File Removed!")

symbols = pd.read_csv('symbol_list.csv',delimiter="\t")
symbols_list = []
for symbol in symbols['Symbol']:
    symbols_list.append(symbol)

#symbols_list = ['F','CX']

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime.today()

symbols=[]
for ticker in symbols_list:	
	r = web.DataReader(ticker,'yahoo',start,end)
	r['8MA'] = r['Close'].rolling(window=8, min_periods=8).mean()
	#r['8EMA'] = r['8MA'].ewm(min_periods=8, alpha=0.222, adjust=False).mean()
	r['20MA'] = r['Close'].rolling(window=20, min_periods=20).mean()
	r['34MA'] = r['Close'].rolling(window=34, min_periods=34).mean()
	r['50MA'] = r['Close'].rolling(window=50, min_periods=50).mean()
	r['200MA'] = r['Close'].rolling(window=200, min_periods=200).mean()
	#r['Change'] = r['Close'] - r['Open']
	#r['PctChange'] = r['Change'] / r['Open']
# add a symbol column
	r['Symbol'] = ticker
	symbols.append(r)
	
# concatenate all the dfs
df = pd.concat(symbols)
#define cell with the columns that i need
cell= df[['Symbol','Open','High','Low','Close','Volume','8MA','20MA','34MA','50MA','200MA']]
#changing sort of Symbol (ascending) and Date(descending) setting Symbol as first column and changing date format
cell.reset_index().sort(['Symbol', 'Date'], ascending=[1,1]).set_index('Symbol').to_csv('raw_data.csv', date_format='%d/%m/%Y')