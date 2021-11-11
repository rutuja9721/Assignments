#Read Data from MYSQL (sales contribution of a product in category)
#and present it using matplotlib (for one category)

import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

connection = mysql.connector.connect(host='localhost',database='retail',user='root',password='Mysql@123')

if(connection.is_connected()):
    print("Connected")
    mycursor = connection.cursor()
    mycursor.execute("select p.product_id, p.description, p.category, sum(t.amt) from product p join tran_dtl t on p.product_id=t.product_id group by p.product_id order by p.category")
    l1 = mycursor.fetchall()
    print(l1)
    l1 = pd.DataFrame(l1)
    l1.columns = ('Product id', 'Product name', 'Category', 'Amount')
    print(l1)
    l1 = l1.loc[l1['Category'] == 'Baked goods']
    plt.pie(l1['Amount'],labels=l1['Product name'], autopct= '%1.1f%%')
    plt.show()
    # for i in l1:
    #     if(i[1] == 'Baked goods'):
    #         l2.append(i)
    #(print(i[2]) for i in l2)
    #plt.pie((i[2] for i in l2), labels=(i[0] for i in l2))
    plt.show()
else:
    print("Error")



