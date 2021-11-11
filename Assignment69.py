#Read retail data from MySQL in to pandas and findout seasonality index for products.

import sqlalchemy as sqla
import pandas as pd
from urllib.parse import quote as urlquote

engine = sqla.create_engine('mysql+pymysql://root:%s@localhost:3306/retail' % urlquote('Mysql@123'))

connection = engine.connect()

result = connection.execute("select product_id, sum(amt), month(tran_dt) from tran_dtl group by product_id,month(tran_dt) order by product_id")

df = pd.DataFrame(result.fetchall())
df.columns = ['Product_Id','Sale_per_month','Month']

result = connection.execute("select product_id,sum(amt) from tran_dtl group by product_id order by product_id")

df1 = pd.DataFrame(result.fetchall())

df1.columns = ['Product_Id','Total_sale']

df = pd.merge(df,df1, on='Product_Id', how='inner')

result = connection.execute("select product_id, count(distinct month(tran_dt)) from tran_dtl group by product_id order by product_id")

df2 = pd.DataFrame(result.fetchall())

df2.columns = ['Product_Id','No_of_seasons']

df = pd.merge(df,df2, on='Product_Id', how='inner')

df['Seasonal_avg'] = df['Total_sale']/df['No_of_seasons']

df['Seasonality_Index'] = df['Sale_per_month']/df['Seasonal_avg']

# pd.set_option('display.max_columns', None)

print(df)
