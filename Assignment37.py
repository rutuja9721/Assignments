#Add a new hard coded column with value = "TEST" to tran_hdr dataframe

#Have included 3 ways to do so

import pandas as pd

df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_hdr_1_2019.csv",header=None)

#df2 = df.assign(new_col = 'TEST')

#df.insert(3,"new_col","TEST",True)

df['new_col'] = 'TEST'

print(df)