"""Plot comparing histograms."""

import pandas as pd
import matplotlib.pyplot as plt
import os

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily return values.		formula: dayret[t] = (price[t]/price[t-0]) - 1"""
    daily_returns = df.copy() #copy given DataFrame to match size and column names
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0,:] = 0 #set daily returns for row 0 to 0 
    return daily_returns
   
def test_run():
 # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')  # one month only
    symbols = ['SPY','IBM']
    df = get_data(symbols, dates)
   
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    
	#compute and plot both histograms on the same chart
    daily_returns['SPY'].hist(bins = 20,label='SPY')
    daily_returns['IBM'].hist(bins = 20,label='IBM')
    plt.legend(loc="upper right")
    plt.show()
	
if __name__ == "__main__":
    test_run()
