#Add new column to tran_dtl dataframe ==> new column is "price" = sales_amt/qty

import pandas as pd

df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

df['Price'] = df['Amount']/df['Quantity']

df1 = df.iloc[:,2:6]

#pd.set_option("display.max_columns",None)

print(df1)