#Read tran_detail file
#Create pandas data frame and do slicing and dicing
#(select only partial columns and rows)

import pandas as pd

df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

print(df.loc[:,['Quantity','Amount','Tran_id']])

print(df.Quantity)

print(df['Quantity'])

print(df[2:4])

print(df[['Quantity','Amount']])


