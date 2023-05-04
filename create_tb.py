import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123',database='pagidala')
cur=mydb.cursor()
t="create table employ(emp_id integer(4),emp_name varchar(20),salary integer(10))"
cur.execute(t)