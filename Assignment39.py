#Filter tran_dtl_dataframe  on qty > 4

import pandas as pd

df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

print(df.loc[(df.Quantity > 4)])