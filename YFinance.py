#https://pypi.org/project/yfinance/
#https://stackoverflow.com/questions/63107594/how-to-deal-with-multi-level-column-names-downloaded-with-yfinance/63107801#63107801

# Purpose: calculate ytd % of change by index

# Current issues
# Issue - yfinance does not have the interval 1 year
# Solution -
# step 1 - Get the right months (3,6,9,12)
# step 2 - Close month 12 minus open month 1
# Step 3 - Calculate difference and percentage
# Wishlist - Flask this to website


# Step 1 - import yfinance
import yfinance as yf

#Step 2 - Data Frame

# download dataframe
# #symbol = yf.Ticker("ndx")
# # use "period" instead of start/end
# # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# print (symbol.history(period="max"))

df = yf.download("ndx", start= '1986-01-01', interval = '3mo', group_by= 'ticker', )
# df['High-Low'] = df['High'] - df['Low']
# df['% change'] = df['High-Low'] / df['Low']
del df['Open']
del df['High']
del df['Low']



#df.reset_index(inplace = False, drop = False)
#df.drop(df.loc[(df.index.month==1) | (df.index.month==4) |   (df.index.month==7)])


#df.dropna(subset = ["Close"], inplace=True)


#df1 = [df.index % 100 == 1]
#df1 = df.drop(index=[0])
#df1 = df[df.index % 1 != 0]

#del df['Adj Close']
#df= df.iloc[::1]
#df= df.iloc[::2]
#df= df.iloc[::3]





#df['Close-Open'] = df['Close'] - df['Open']
#df['% change'] = df['Close-Open'] / df['Open']




#print(data)
df.to_csv('yahoo.csv')
print(df)
