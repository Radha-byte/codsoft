import tkinter as tk
from tkinter import messagebox

todo_list=[]
def add_task():
    task = entry.get()
    if task:
        todo_list.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Task cannot be empty!")
def delete_task():
    try:
        index = listbox.curselection()[0]
        todo_list.pop(index)
        listbox.delete(index)
    except:
        messagebox.showwarning("Error", "No task selected!")
def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = todo_list[index] + " COMPLETED"
        listbox.delete(index)
        listbox.insert(index, task)
        listbox.itemconfig(index, {'fg': 'green'})
    except:
        messagebox.showwarning("Error", "No task selected!")

root = tk.Tk()
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

for text, cmd in [("Add Task", add_task), ("Delete Task", delete_task), ("Mark Completed", mark_completed)]:
    tk.Button(root, text=text, command=cmd).pack(pady=5)
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
root.mainloop()
