import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='chandra80',database='pythondb')

if conn.is_connected():
    print("Connection Established")

mycursor = conn.cursor()

# mycursor.execute('create database pythondb')

mycursor.execute('create  table student (name varchar(50),branch varchar(10),id int)')
mycursor.execute('show tables')

print(mycursor)

for x in mycursor:
    print(x)


