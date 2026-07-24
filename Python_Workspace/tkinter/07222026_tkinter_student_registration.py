import tkinter as tk
from tkinter import ttk, messagebox
import Constants as cst
import StudentRegistration as std_reg
from student import Student

def on_click_add_student():
    new_student = Student(e2.get(),e3.get(),e4.get())
    std_reg.add_student(new_student,show_success_message)

def on_click_update():
    new_student = Student(e2.get(),e3.get(),e4.get(),e1.get())
    std_reg.update_student_details(new_student,show_success_message)

def on_click_delete():
    new_student = Student(e2.get(),e3.get(),e4.get(),e1.get())
    std_reg.delete_student_details(new_student,show_success_message)

def load_all_details():
    std_reg.load_all_student_details(load_student_details)

def show_success_message(title, message):
    load_all_details()
    messagebox.showinfo(title,message)

    # clear all the text fields
    e1.delete(0, tk.END)
    e1.config(state="disabled")
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

def load_student_details(student_details_row):
    # Tree view to display all the data
    global listBox
    listBox = ttk.Treeview(root,columns=cst.ALL_COLUMNS,show="headings")
    listBox.grid(row=7,column=0,columnspan=3,padx=10,pady=10)
    for col in cst.ALL_COLUMNS:
        listBox.heading(col, text=col)
        listBox.column(col, width=150)

    # Bind the select event to populate entry fields when a row is clicked
    listBox.bind("<ButtonRelease-1>", on_treeview_select)

    for row in student_details_row:
        listBox.insert("", "end", values=row)

    listBox.bind("<ButtonRelease-1>", on_treeview_select)



# Function to populate the entry fields when a row is selected
def on_treeview_select(event):
    print("inside the on_treeview_select() ::::::::::")
    global listBox
    selected_item = listBox.selection()
    print("inside the on_treeview_select() ::::::::::selected_item = ",selected_item)
    
    if selected_item and len(selected_item) > 0:
        student = listBox.item(selected_item)
        studentid, studentname, coursename, fee = student['values']
       
        # Populate the entry fields with the selected student's data
        e1.config(state="normal")  # Make the ID entry editable to update
        e1.delete(0, tk.END)
        e1.insert(0, studentid)  # Set the student ID for deletion or update

        e2.delete(0, tk.END)
        e2.insert(0, studentname)

        e3.delete(0, tk.END)
        e3.insert(0, coursename)

        e4.delete(0, tk.END)
        e4.insert(0, fee)
    else:
        print("inside the on_treeview_select() :::::::ELSE BLOCK = ",selected_item)
        


root = tk.Tk()

root.geometry("700x700")
root.title(cst.TITLE)

tk.Label(root, text = cst.LABEL_STUDENT_ID).grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text = cst.LABEL_STUDENT_NAME).grid(row=1,column=0,padx=10,pady=10)
tk.Label(root, text = cst.LABEL_STUDENT_COURSE).grid(row=2,column=0,padx=10,pady=10)
tk.Label(root, text = cst.LABEL_STUDENT_FEES).grid(row=3,column=0,padx=10,pady=10)


e1=tk.Entry()
e1.grid(row=0,column=1,padx=10,pady=10)
e1.config(state="disabled")

e2 = tk.Entry()
e2.grid(row=1,column=1,padx=10,pady=10)
e2.config(state="normal")

e3 = tk.Entry()
e3.grid(row=2, column=1, padx=10,pady=10)
e3.config(state="normal")

e4=tk.Entry()
e4.grid(row=3, column=1, padx=10, pady=10)
e4.config(state="normal")


tk.Button(root,text=cst.BUTTON_ADD,command= on_click_add_student).grid(row=5, column=0,padx=10,pady=10)
tk.Button(root,text=cst.BUTTON_UPDATE, command=on_click_update).grid(row=5, column=1,padx=10,pady=10)
tk.Button(root,text=cst.BUTTON_DELETE, command=on_click_delete).grid(row=5, column=2,padx=10,pady=10)


listBox= ttk.Treeview(root,show="headings")
# listBox.bind("<ButtonRelease-1>", on_treeview_select)

load_all_details()

root.mainloop()


