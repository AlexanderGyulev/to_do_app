import tkinter as tk


class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("To Do App")
        self.root.geometry("600x600")
        self.build_ui()
        self.refresh_list()

    def build_ui(self):
        self.text_entry = tk.Entry(self.root)
        self.text_entry.pack()
        self.add_button = tk.Button(self.root, text="Add a task", command=self.on_add)
        self.add_button.pack()
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(fill="both", expand=True)
        self.delete_button = tk.Button(self.root, text="Delete a task", command=self.on_delete)
        self.delete_button.pack()
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def on_add(self):
        text = self.text_entry.get()
        if len(text) == 0: # check if the text_entry contains any text
            self.status_label.configure(text="Task cannot be empty")
            return
        self.task_manager.add_task(text)
        self.refresh_list()
        self.status_label.configure(text="Task added")

    def on_delete(self):
        index = self.task_listbox.curselection()
        if len(index) == 0: # check if the tuple above is empty, avoiding IndexErrors
            self.status_label.configure(text="Please select a task first")
            return
        self.task_manager.delete_task(index[0]) # curselection returns a tuple, not an index
        self.refresh_list()
        self.status_label.configure(text="Task deleted")

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(tk.END, task)

