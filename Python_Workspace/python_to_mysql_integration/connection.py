import mysql.connector
conn = mysql.connector.connect(host='localhost',user ='root',password ='chandra80')

if conn.is_connected():
    print('Connection Established')
print(conn)
print(conn.is_connected())