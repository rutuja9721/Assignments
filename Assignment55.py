#Try pie-chart and other visualizations on Retail data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Python\\tran_dtl_1_2019.csv",header=None)

df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']

top = df.groupby(['Product_id'], as_index = False).sum()

top1 = top.sort_values(by = ['Amount'], ascending=False).iloc[0:5]
print(top1)

plt.pie(top1['Amount'],labels = top1['Product_id'])
plt.title('Distribution of sale by product_id')
plt.show()

plt.figure()
plt.boxplot(top1['Amount'])
plt.show()

plt.scatter(top1['Product_id'],top1['Amount'], c="blue")
plt.show()