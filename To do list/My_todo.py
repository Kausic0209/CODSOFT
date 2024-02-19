#lets make todo list

#for providing gui
import tkinter as tk

#for add task function
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

#for edit task function
def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        selected_task = listbox_tasks.get(task_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, selected_task)
        delete_task()
    except IndexError:
        pass

#for delete task function
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

#for complete task function
def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'light green'})
    except IndexError:
        pass

root = tk.Tk()
root.title("My To-Do List") #for title

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=12)

#background of task
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="light blue", fg="blue", border=0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

#for color  click function of add task button
button_add_task = tk.Button(frame_buttons, text="Add Task", command=add_task, bg="orange", fg="white")
button_add_task.pack(side=tk.LEFT)

#for color  click function of edit task button
button_edit_task = tk.Button(frame_buttons, text="Edit Task", command=edit_task, bg="orange", fg="white")
button_edit_task.pack(side=tk.LEFT)

#for color  click function of delete task button
button_delete_task = tk.Button(frame_buttons, text="Delete Task", command=delete_task, bg="orange", fg="white")
button_delete_task.pack(side=tk.LEFT)

#for color  click function of complete task button
button_complete_task = tk.Button(frame_buttons, text="Complete Task", command=complete_task, bg="orange", fg="white")
button_complete_task.pack(side=tk.LEFT)

root.mainloop()
#THANK YOU.