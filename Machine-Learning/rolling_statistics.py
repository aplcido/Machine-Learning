"""Rolling statistics"""

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
    symbols = ['SPY']
    
    # Get stock data
    df = get_data(symbols, dates)
	
	#plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean",label='SPY')
	
	#compute rolling mean using a 20-day window
    rm_SPY = df['SPY'].rolling(window=20).mean()
	
	#add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean',ax=ax)
	
	#add axis labels and legend
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()
	
    print (df)


if __name__ == "__main__":
    test_run()