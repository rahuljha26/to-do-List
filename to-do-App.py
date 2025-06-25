from tkinter import *
from tkinter import messagebox


win = Tk()
win.title("To-Do App")
win.geometry("400x450")
win.config(bg="lightgray")

tasks = []


def show_tasks():
    Lstbox.delete(0, END)
    for i, item in enumerate(tasks):
        Lstbox.insert(END, f"{i + 1}. {item}")

def add_task():
    new_task = entry_task.get().strip()
    if new_task:
        tasks.append(new_task)
        entry_task.delete(0, END)
        show_tasks()

def delete_task():
    try:
        index = Lstbox.curselection()[0]
        tasks.pop(index)
        show_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def select_task():
    try:
        index = Lstbox.curselection()[0]
        print("Selected Task:", tasks[index])
    except IndexError:
        print("No task selected.")

def edit_task():
    try:
        index = Lstbox.curselection()[0]
        old_task = tasks[index]
        new_text = entry_task.get().strip()
        if new_text:
            confirm = messagebox.askyesno("Confirm Edit", f"Replace:\n'{old_task}'\nwith\n'{new_text}'?")
            if confirm:
                tasks[index] = new_text
                entry_task.delete(0, END)
                show_tasks()
        else:
            messagebox.showinfo("Info", "Please enter new task text to update.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

label = Label(win, text="Enter a task:", bg="lightgray", font=("Arial", 12))
label.pack(pady=(15, 0))

entry_task = Entry(win, width=40, font=("Arial", 12))
entry_task.pack(pady=8)
entry_task.bind("<Return>", lambda event: add_task())  # BINDING ENTER KEY

Lstbox = Listbox(win, width=50, height=10, font=("Arial", 12))
Lstbox.pack(pady=10)

btn_add = Button(win, text="Add Task", width=20, bg="lightblue", font=("Arial", 10), command=add_task)
btn_add.pack(pady=5)

btn_delete = Button(win, text="Delete Task", width=20, bg="salmon", font=("Arial", 10), command=delete_task)
btn_delete.pack(pady=5)

btn_edit = Button(win, text="Edit Task", width=20, bg="orange", font=("Arial", 10), command=edit_task)
btn_edit.pack(pady=5)

btn_select = Button(win, text="Select Task", width=20, bg="lightgreen", font=("Arial", 10), command=select_task)
btn_select.pack(pady=5)

show_tasks()

win.mainloop()
