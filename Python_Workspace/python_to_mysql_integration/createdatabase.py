import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='chandra80')

if conn.is_connected():
    print("Connection Established")

mycursor = conn.cursor()

mycursor.execute('create database pythondb')
print(mycursor)

# mycursor.execute('show databases')
# for x in mycursor:
#     print(x)
