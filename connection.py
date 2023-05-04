import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123')
print(mydb.connection_id)