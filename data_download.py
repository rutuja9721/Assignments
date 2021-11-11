import pandas as pd
from nsepy import get_history
from datetime import date
import os

# file_dir = r"E:/"
# url='https://www.nseindia.com/market-data/securities-available-for-trading/EQUITY_L.csv'
symbol = pd.read_csv('EQUITY_L.csv') #csv containing list of symbols of shares
symbol_list = symbol['SYMBOL']
# filename = file_dir + str(date.today()) + "_Market_data.csv"
# print("filename: " + filename)

symbol_df = pd.DataFrame()
# print(ns.get_history(symbol='infy',start=date(2021,9,10),end=date(2021,9,10)))
for i in symbol_list:
    # print(i)
    # print(ns.get_history(symbol=str(i),start=date(2021,9,13),end=date(2021,9,13)))
    df = get_history(symbol=str(i), start=date(2021, 7, 1), end=date.today())
    df = pd.DataFrame(df)
    symbol_df = pd.concat([symbol_df, df])
print(symbol_df.head(3))
# symbol_df.to_csv(filename)
