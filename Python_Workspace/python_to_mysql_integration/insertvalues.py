import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='chandra80',database='pythondb')

if conn.is_connected():
    print("Connection Established")

mycursor = conn.cursor()
mycursor.execute('use pythondb')

sql_query = "INSERT INTO student (name,branch,id) VALUES (%s, %s, %s)"

val = [('john','CSE','56'),('Mike','IT','78'),('Tyson','ME','80')]

mycursor.executemany(sql_query,val)
conn.commit()

print( mycursor.rowcount,'record inserted')




# select query
select_sql_query = "SELECT * FROM student WHERE id = %s"

param = (78,)
print(param)

mycursor.execute(select_sql_query,param)
results = mycursor.fetchall()
print("results = ",results)

if results:
    print(f"Success! Found {len(results)} records.")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, branch: {row[2]}")
else:
    print(" No records found (results is empty)")





