import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123',database='pagidala')
cur=mydb.cursor()
t="insert into employ(emp_id,emp_name,salary) values(%s,%s,%s)"
a=[(109,'James',10003),(101,'Kumar',10001),(102,'Kound',10002)]
cur.executemany(t,a)
mydb.commit()
print("data insertd successfully")