#Join tran_hdr, and tran_detail dataframes using pandas (try inner, outer, left outer, right outer joins)

import pandas as pd

# hdr = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_hdr_1_2019.csv",header=None)
#
# hdr.columns = ['Tran_id','Store_id','Member_id','Tran_date']
#
# dtl = pd.read_csv("D:\MySql\mysql\Retail_Data\\tran_dtl_1_2019.csv",header=None)
#
# dtl.columns = ['Tran_id','Product_id','Quantity','Amount','Tran_date']


c = {'id': [1, 2, 3, 4],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(c)

d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a,b, on = 'id', how='inner')

df1 = pd.merge(a,b, on = 'id', how='left')

df2 = pd.merge(a,b, on = 'id', how='right')

df3 = pd.merge(a,b, on = 'id', how='outer')

print(df)
print(df1)
print(df2)
print(df3)