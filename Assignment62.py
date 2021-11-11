#Create Table product, Month, TotalSale in mySQl
#Read retail transaction table from MySQL in to pandas dataframe
#Compute product, month, total sale and insert in to the table

from urllib.parse import quote as urlquote
import mysql.connector
import pandas as pd
import sqlalchemy as sqla

#engine = sqla.create_engine('mysql+mysqlconnector://root:%s@localhost:3306/retail' % urlquote('Mysql@123'))
engine = sqla.create_engine('mysql+pymysql://root:%s@localhost:3306/retail' % urlquote('Mysql@123'))

connection = engine.connect()

result = connection.execute("select product_id, month(tran_dt), sum(amt) from tran_dtl group by month(tran_dt), product_id order by month(tran_dt), product_id")
df = pd.DataFrame(result.fetchall())
df.columns = ['product_id','month','total_sale']
df.to_sql(con = connection, name='example2', if_exists='append', index=False)

# metadata = sqla.MetaData()
# dept = sqla.Table('product',metadata,autoload=True,autoload_with=engine)

# print(dept.columns.keys())

# engine = sqlalchemy.create_engine('mysql+pymysql://root:Mysql@123@localhost:3306/retail')


# connection = mysql.connector.connect(host='localhost', user='root', password='Mysql@123', database='retail')
#
# if connection.is_connected():
#     print("Connected")
#
# else:
#     print("Not connected")
#
# from sqlalchemy import create_engine
# mycursor = connection.cursor()
# mycursor.execute("select product_id, month(tran_dt), sum(amt) from tran_dtl group by month(tran_dt), product_id order by month(tran_dt), product_id")
# df = pd.DataFrame(mycursor.fetchall())
# df.columns = ['product_id','month','total_sale']
# # df.to_sql("example",con=connection, index=False, if_exists='append')
# engine = sqlalchemy.create_engine('mysql+pymysql://root:Mysql@123@localhost:3306/retail')
# df.to_sql('example',engine,if_exists='append')
# print
