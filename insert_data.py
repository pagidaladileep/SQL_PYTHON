import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123',database='pagidala')
cur=mydb.cursor()
t="insert into employ(emp_id,emp_name,salary) values(%s,%s,%s)"
a=(100,'dileep',10000)
cur.execute(t,a)
mydb.commit()
print("data insertd successfully")