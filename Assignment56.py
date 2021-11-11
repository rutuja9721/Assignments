#Read data from MySQL, store data in pandas dataframe, assign variables for every column,
#plot graph accordingly. ( refer documentation for Matplotlib )

from urllib.parse import quote as urlquote
import pandas as pd
import sqlalchemy as sqla
import matplotlib as plt

engine = sqla.create_engine('mysql+pymysql://root:%s@localhost:3306/emp' % urlquote('Mysql@123'))

connection = engine.connect()

result = connection.execute("select dept_no, count(emp_no) from dept_emp group by dept_no limit 20;")
df = pd.DataFrame(result.fetchall())

df.columns = ['Dept_no','No_of_employees']

print(df)

plt.pie(df['No_of_employees'],labels=df['Dept_no'], autopct= '%1.1f%%')

plt.show()