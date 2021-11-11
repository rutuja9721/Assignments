#Read transaction_hdr(1_jan_2019) data and convert it into pandas dataframe
#Similarly read transaction_dtl_data (1_jan_2019)

import pandas as pd

df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

print(df)

df1 = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_hdr_1_2019.csv",header=None)

df1.columns = ['Tran_id','Store_id','Member_id','Tran_date']

print(df1)