#Find profile of numerical variable (min, max, quantile, mean, median, standard deviation) using pandas

import numpy as np
import pandas as pd

# df = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)
#
# df.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']
#
# print(df.describe())

s = pd.Series([2,3,4])

print(s.describe())

print(s.median())

print(np.quantile(s,0.25))

print(np.percentile(s,90))