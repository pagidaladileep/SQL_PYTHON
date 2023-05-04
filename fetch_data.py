import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123',database='pagidala')
cur=mydb.cursor()
f='select * from employ where emp_id=101'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)
