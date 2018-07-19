import pandas as pd 

def test_run():
    #define data range
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)
	
    #Create an empty dataframe
    df1=pd.DataFrame(index=dates)	
	
    #read SPY data into temporary dataframe
    dfSPY = pd.read_csv('data/SPY.csv',index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
    print (dfSPY)
	
    #join the two dataframes using DataFrame.join
    df1=df1.join(dfSPY)
    
    #drop Nan values
    df1=df1.dropna()
    print (df1)

	
	
if __name__ == '__main__':
    test_run()