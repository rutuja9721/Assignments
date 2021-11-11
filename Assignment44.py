#Add some missing values in raw data in tran_dtl file (create a separate file)
#Read this file, create a pandas dataframe and replace missing value with 1.
#Default value, forward fill, backward fill.

import pandas as pd

df = pd.read_csv("D:\Python\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

print(df.fillna('1'))

print("\n")
print("\n")
print("\n")

# print(df.ffill(axis=0))
# #print(df.ffill(axis=0)) To fill values found in previous column of same row
#
# print("\n")
# print("\n")
#
# print(df.bfill(axis=0))

print(df.fillna(method='bfill'))


