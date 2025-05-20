import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        pass

root = tk.Tk()
root.title("To-Do List Sederhana")
root.geometry("300x350")

frame_title = tk.Frame(root)
frame_title.pack(pady=10)

title = tk.Label(frame_title, text="To-Do List", font=("Arial", 12))
title.pack()

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

entry = tk.Entry(frame_input, width=25)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame_input, text="Tambah", command=add_task)
add_button.pack(side=tk.LEFT)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame_tasks, width=40, height=12)
listbox.pack(fill=tk.BOTH, expand=True, padx=10)

delete_button = tk.Button(root, text="Hapus Tugas", command=delete_task)
delete_button.pack(pady=10)

root.mainloop()