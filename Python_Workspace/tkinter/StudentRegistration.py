import tkinter as tk
import tkinter as messagebox
from student import Student
import sql_queries as sql
import mysql.connector

# Function to create a database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='chandra80',
        database='webgui'
    )



def add_student(student, callback):
    # std_name = student.name()
    # std_course = student.course()
    # std_fees = student.fees()
    # print("Student Details : ",std_name,std_course,std_fees)
    print(str(student))
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        values = (student.name(), student.course(), student.fees())
        cursor.execute(sql.INSERT_NEW_STUDENT,values)
        conn.commit()
               
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to insert student: {err}")
    else:
        callback("Success","Student record added successfully!")
    finally:
        conn.close()


def update_student_details(student,callback):
    print(str(student))
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        values = (student.name(), student.course(), student.fees(),student.id())
        cursor.execute(sql.UPDATE_STUDENT_DETAILS,values)
        conn.commit()
               
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to update student: {err}")
    else:
        callback("Success","Sucessfully UPDATED the record")
    finally:
        conn.close()

def delete_student_details(student,callback):
    print(str(student))
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        values=(student.id(),)

        cursor.execute(sql.DELETE_STUDENT_DETAILS,values)
        conn.commit()
               
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to delete student: {err}")
    else:
        callback("Success","Sucessfully DELETED the record")
    finally:
        conn.close()


def load_all_student_details(callback):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql.SELECT_ALL_STUDENT)
        all_students_rows = cursor.fetchall()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to load student: {err}")
    else:
        callback(all_students_rows)
    finally:
        conn.close()

    

