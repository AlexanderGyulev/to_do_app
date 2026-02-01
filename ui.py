import tkinter as tk

class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("To Do App")
        self.root.geometry("600x600")
        self.build_ui()
    def build_ui(self):
        self.text_entry = tk.Entry(self.root)
        self.text_entry.pack()
        self.add_button = tk.Button(text="Add a task", command=self.on_add)
        self.add_button.pack()
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()
        self.delete_button = tk.Button(text="Delete a task")
        self.delete_button.pack()
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()
    def on_add(self):
        text = self.text_entry.get()
        self.task_manager.add_task(text)
        self.refresh_list()
    def refresh_list(self):
        pass
