
import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("400x200")

def say_hello():
    print('Hello world !! tkinter button clicked!!')

hello_button = tk.Button(root,text="Click Me", command=say_hello)
hello_button.pack(pady = 20)

root.mainloop()

