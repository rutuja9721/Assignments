#Get Data from NSE Api and insert data into MYSQL database with duplication check

from nsepy import get_history
from datetime import date
import pandas as pd

symbol = pd.read_csv("EQUITY_L.csv")
symbol_list = symbol['SYMBOL']
# print(symbol_list)

symbol_df = pd.DataFrame()

for i in symbol_list:
    df = get_history(symbol = i, start=date(2021,7,1), end=date.today())
    symbol_df = pd.concat([symbol_df, df])

print(symbol_df.head(3))

symbol_df.to_csv("example.csv")

# data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
#
# data[['Close']].plot()
#
# sbin = get_history(symbol='SBIN',
#                    start=date(2015,1,1),
#                    end=date(2015,1,10))
#
# print(sbin)

