#Read same file from 37
#Create pandas dataframe and replace missing values with separate values for each column
#(use different strategies of imputation)

import pandas as pd

df = pd.read_csv("D:\Python\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

#print(df.fillna(df['Product_id'].value_counts().index[0]))

#print(df.apply(lambda x:x.fillna(x.value_counts().index[0])))

#print(df.fillna(df.mode().iloc[0]))

#rint(df.fillna(df.select_dtypes(include='object').mode().iloc[0]))

#print(df.fillna(df.select_dtypes(include='number').mean().iloc[0]))

print(df.fillna({'Tran_id':df['Tran_id'].mode().iloc[0], 'Product_id':df['Product_id'].mean()}))



