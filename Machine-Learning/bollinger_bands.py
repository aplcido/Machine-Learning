"""Calculating bollinger bands."""

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

def get_rolling_mean(values,window):
   """Return rolling mean of given values, using specified window size"""
   return values.rolling(window=window).mean() 
   
def get_rolling_std(values,window):
   """Return rolling standard deviation of given values, using specified window size"""
   return values.rolling(window=window).std()  

def get_bollinger_bands(rm,rstd):
   """Return upper and lower Bollinger bands."""
   upper_band = rm + rstd * 2
   lower_band = rm - rstd * 2
   return upper_band, lower_band     
   
def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['SPY']
    
    # Get stock data
    df = get_data(symbols, dates)
	
	#compute Bollinger bands
	#1 - compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'],window=20)
	
	#2 - compute rolling std
    rstd_SPY = get_rolling_std(df['SPY'],window=20)
	
	#3 - compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY,rstd_SPY)
	
	#plot raw SPY values, rolling mean and Bollinger bands
    ax = df['SPY'].plot(title="Bollinger bands",label='SPY')
    rm_SPY.plot(label="Rolling mean", ax=ax)
    upper_band.plot(label="Upper band", ax=ax)
    lower_band.plot(label="Lower band", ax=ax)
	 
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()
	
    print (df)


if __name__ == "__main__":
    test_run()