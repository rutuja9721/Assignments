#Read Retail Data Csv and plot sale for top 5 produts using matplot lib (bar charts)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Python\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

top = df.groupby(['Product_id'],as_index=False).sum()

#top = df[['Product_id','Amount']]

top1 = top.sort_values(by=['Amount'], ascending=False).iloc[0:6]

plt.bar(x=top1['Product_id'],height=top1['Amount'])

plt.show()


