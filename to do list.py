import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        # Initialize task list
        self.tasks = []

        # Create GUI components
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=30, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, font=("Helvetica", 14))
        self.task_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.root, text="Mark as Complete", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.uncomplete_task_button = tk.Button(self.root, text="Mark as Uncomplete", command=self.uncomplete_task)
        self.uncomplete_task_button.pack(pady=5)

        # Tracking Labels
        self.total_tasks_label = tk.Label(self.root, text="Total Tasks: 0", font=("Helvetica", 12))
        self.total_tasks_label.pack(pady=5)

        self.completed_tasks_label = tk.Label(self.root, text="Completed Tasks: 0", font=("Helvetica", 12))
        self.completed_tasks_label.pack(pady=5)

        self.remaining_tasks_label = tk.Label(self.root, text="Remaining Tasks: 0", font=("Helvetica", 12))
        self.remaining_tasks_label.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"name": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.update_task_counts()
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
            self.update_task_counts()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_listbox()
            self.update_task_counts()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    def uncomplete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = False
            self.update_task_listbox()
            self.update_task_counts()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as uncomplete.")

    def update_task_listbox(self):
        # Clear the current list
        self.task_listbox.delete(0, tk.END)

        # Add updated tasks to the listbox
        for task in self.tasks:
            task_text = task["name"]
            if task["completed"]:
                task_text += " (Completed)"
            self.task_listbox.insert(tk.END, task_text)

    def update_task_counts(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        remaining_tasks = total_tasks - completed_tasks

        self.total_tasks_label.config(text=f"Total Tasks: {total_tasks}")
        self.completed_tasks_label.config(text=f"Completed Tasks: {completed_tasks}")
        self.remaining_tasks_label.config(text=f"Remaining Tasks: {remaining_tasks}")

# Create the application window and start the GUI loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
