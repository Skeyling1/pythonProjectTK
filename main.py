import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def up_task():
    selected_task_index = task_list.curselection() #2
    selected_task = task_list.get(selected_task_index) #получаем индекс
    task_list.delete(selected_task_index)
    for item in selected_task_index:
        task_list.insert(item-1, selected_task)

def down_task():
    selected_task_index = task_list.curselection() #2
    selected_task = task_list.get(selected_task_index) #получаем индекс
    task_list.delete(selected_task_index)
    for item in selected_task_index:
        task_list.insert(item+1, selected_task)

def mark_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, bg="chartreuse4")

root = tk.Tk()
root.title("Task list")
root.configure(background="burlywood2")
text2 = tk.Label(root, text="Впишите задачу", bg="burlywood2")
text2.pack()
task_entry = tk.Entry(root, width=35, bg="white", fg="black")
task_entry.pack(pady=10, padx=10)
butt_1 = tk.Button(root, width=30, text="Add task", bg="aquamarine1", fg="black", command=add_task)
butt_1.pack(pady=10, padx=10)
butt_delete = tk.Button(root, width=30, text="Delete task", bg="coral2", fg="black", command=delete_task)
butt_delete.pack(pady=10, padx=10)
butt_mark = tk.Button(root, width=30, text="Mark complete task", bg="chartreuse4", fg="black", command=mark_task)
butt_mark.pack(pady=10, padx=10)
butt_up = tk.Button(root, width=5, text="Up", bg="dark turquoise", fg="black", command=up_task)
butt_up.pack(pady=1, padx=10)
butt_down = tk.Button(root, width=5, text="Down", bg="dark turquoise", fg="black", command=down_task)
butt_down.pack(pady=1, padx=10)
text2 = tk.Label(root, text="Список задач", bg="burlywood2")
text2.pack()
task_list = tk.Listbox(root, width=35, height=20, bg="white", fg="black")
task_list.pack(pady=10, padx=10)
root.mainloop()