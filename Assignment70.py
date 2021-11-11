#Read retail data from MySQL in to pandas calculate total purchase by member per month
#and remove outliers from the data.

import sqlalchemy as sqla
import pandas as pd
from urllib.parse import quote as urlquote
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

engine = sqla.create_engine('mysql+pymysql://root:%s@localhost:3306/retail' % urlquote('Mysql@123'))

connection = engine.connect()

result = connection.execute("select th.member_id, month(th.tran_dt), sum(td.amt) from tran_hdr th join tran_dtl td on th.tran_id=td.tran_id group by th.member_id, month(th.tran_dt) order by th.member_id")

df = pd.DataFrame(result.fetchall())

df.columns = ['Member_id','Month','Purchase']

# sb.scatterplot(data=df,x="Month",y="Purchase")

# sb.boxplot(data=df,x="Month",y="Purchase", showfliers = False)
# sb.boxplot(data=df,x="Month",y="Purchase")

quant = pd.DataFrame()

quant['Q1'] = df.groupby('Month')['Purchase'].quantile(0.25)
quant['Q3'] = df.groupby('Month')['Purchase'].quantile(0.75)
quant['Max'] = quant['Q3']+(1.5*(quant['Q3']-quant['Q1']))
quant['Min'] = quant['Q1']-(1.5*(quant['Q3']-quant['Q1']))

df = pd.merge(df,quant, on='Month', how='inner')

pd.set_option('display.max_rows', None)

df['Purchase'] = np.where(df.Purchase>df.Max,df.Max,df.Purchase)

# filter = df['Purchase']<df['Max']
#
# print(filter)
#
# df.where(filter, inplace=True)

print(df)

sb.boxplot(data=df,x="Month",y="Purchase")

plt.show()


