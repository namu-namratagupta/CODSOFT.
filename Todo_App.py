import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import json

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")

        # Task lists
        self.tasks = []
        self.completed_tasks = []

        # Create GUI elements
        self.task_entry_label = tk.Label(master, text="Task:")
        self.task_entry_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        self.task_listbox_label = tk.Label(master, text="To-Do List:")
        self.task_listbox_label.grid(row=1, column=0, padx=10, pady=5, columnspan=3)

        self.task_listbox = tk.Listbox(master, width=50, height=15, bg='#333', fg='white', selectbackground='#555', selectforeground='white')
        self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.completed_listbox_label = tk.Label(master, text="Completed Tasks:")
        self.completed_listbox_label.grid(row=3, column=0, padx=10, pady=5, columnspan=3)

        self.completed_listbox = tk.Listbox(master, width=50, height=5, bg='lightgreen', fg='black')
        self.completed_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.remove_button = ttk.Button(master, text="Remove Task", command=self.remove_task, style="TButton")
        self.remove_button.grid(row=5, column=0, padx=10, pady=10)

        self.complete_button = ttk.Button(master, text="Mark Complete", command=self.mark_complete, style="TButton")
        self.complete_button.grid(row=5, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(master, text="Save Tasks", command=self.save_tasks, style="TButton")
        self.save_button.grid(row=5, column=2, padx=10, pady=10)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            new_task = {"title": task_title, "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "completed": False}
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, self.format_task_text(new_task))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = not task["completed"]
            self.update_task_text(selected_index[0])
            if task["completed"]:
                self.completed_tasks.append(task)
                self.completed_listbox.insert(tk.END, self.format_task_text(task, completed=True))
            else:
                completed_index = self.completed_tasks.index(task)
                self.completed_tasks.pop(completed_index)
                self.completed_listbox.delete(completed_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump({"tasks": self.tasks, "completed_tasks": self.completed_tasks}, file, indent=2)
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                data = json.load(file)
                self.tasks = data.get("tasks", [])
                self.completed_tasks = data.get("completed_tasks", [])
        except FileNotFoundError:
            self.tasks = []
            self.completed_tasks = []

        for task in self.tasks:
            self.task_listbox.insert(tk.END, self.format_task_text(task))
            if task['completed']:
                self.task_listbox.itemconfig(tk.END, {"fg": "gray"})

        for completed_task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, self.format_task_text(completed_task, completed=True))

    def format_task_text(self, task, completed=False):
        checkbox = "[X]" if completed or task["completed"] else "[ ]"
        return f"{checkbox} {task['title']}"

    def update_task_text(self, index):
        task = self.tasks[index]
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, self.format_task_text(task))
        if task['completed']:
            self.task_listbox.itemconfig(index, {"fg": "gray"})

def main():
    root = tk.Tk()
    app = ToDoApp(root)

    # Style the buttons with a dark theme
    style = ttk.Style()
    style.configure("TButton", foreground="black", background="black", padding=10)

    root.mainloop()

if __name__ == '__main__':
    main()
