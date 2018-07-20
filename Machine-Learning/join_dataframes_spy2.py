"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df,columns,start_index,end_index):
   """Plot the desired columns over index values in the defined range"""
   plot_data(df.ix[start_index:end_index,columns],title="Selected data")

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp)
        if(symbol=='SPY'): #drop dates where SPY did not trade
           df = df.dropna(subset=['SPY'])
		
    return df


def normalize_values(df):
   """Normalize stock prices using the first row of the dataframe."""
   return df/ df.ix[0,:]

def plot_data(df,title="Stock Prices"):
   """Plot stock prices"""
   ax = df.plot(title=title, fontsize=12)
   ax.set_xlabel("Date")
   ax.set_ylabel("Price")
   plt.show() #must be called to show plot in some environments

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)

    #normalize_values(df)
    
    
	#slice and plot
    plot_selected(df,['SPY','IBM'],'2010-03-01','2010-04-01')
    
	#slice by row range (dates) using DataFrame.ix[] selector
    #print df.ix['2010-01-01':'2010-12-31'] # the month of January
    
    #slice by columns(symbols)
    #print df.ix['GOOG'] # a single label that selects a single column
    #print df.ix[['IBM,GLD']] # a list of labels selects multiple columns
    
    #slice by row and column
    #print (df.ix['2010-01-01':'2010-12-31',['SPY','IBM']])
    print (df)


if __name__ == "__main__":
    test_run()
