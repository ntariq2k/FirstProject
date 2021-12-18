#https://pypi.org/project/yfinance/
#https://stackoverflow.com/questions/63107594/how-to-deal-with-multi-level-column-names-downloaded-with-yfinance/63107801#63107801

# Purpose: pull ytd data by index and calculate the % of difference
# Step 1 - import yfinance
# Step 2 - dataframe


# Current issues
# step 1 - Get the right months (3,6,9,12)
# step 2 - Only 12
# Step 3 - Calculate difference and percentage


# #symbol = yf.Ticker("ndx")
# # use "period" instead of start/end
# # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# print (symbol.history(period="max"))



#test change onto github

import yfinance as yf
# download dataframe
df = yf.download("ndx", period='max', interval = '3mo', group_by= 'ticker', )
# df['High-Low'] = df['High'] - df['Low']
# df['% change'] = df['High-Low'] / df['Low']

df['Open-Close'] = df['Open'] - df['Close']
df['% change'] = df['Open-Close'] / df['Open']

#data = yf.download(tickers = "SPY AMZN", period='6mo')
#print(data)
df.to_csv('yahoo.csv')
print(df)
#print(df.columns)print(df)