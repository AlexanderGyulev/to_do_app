import os
import tkinter as tk
from ui import ToDoApp


class TaskManager:

    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.task_list = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                for element in f:
                    self.task_list.append(element.strip())

    def save_tasks(self):
        with open(self.storage_path, "w") as f:
            for element in self.task_list:
                f.write(element + "\n")

    def add_task(self,text):
        self.task_list.append(text)
        self.save_tasks()

    def delete_task(self,index):
        self.task_list.pop(index)
        self.save_tasks()

    def clear_all_tasks(self):
        self.task_list = []
        self.save_tasks()

    def get_tasks(self):
        return self.task_list


if __name__ == '__main__':
    root = tk.Tk()
    storage_file = "tasks.txt"
    manager = TaskManager(storage_file)
    app = ToDoApp(root, manager)
    root.mainloop()
