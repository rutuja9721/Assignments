from urllib.parse import quote as urlquote
import pandas as pd
import sqlalchemy as sqla

engine = sqla.create_engine('mysql+pymysql://root:%s@localhost:3306/joins' % urlquote('Mysql@123'))

connection = engine.connect()

df = pd.read_csv("Employee_table_final.csv")

emp = df[['Emp_id','First_Name','Last_Name','Gender_id','Dept_ID','Mob_No','Email_Id','Pincode','Manager_id','Hire_date','Salary','Friend_id']]

emp.to_sql(con=connection, name = 'employee', if_exists='append',index=False)

# print(df.columns)