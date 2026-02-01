import tkinter as tk
from ui import ToDoApp

class TaskManager:
    def __init__(self):
        self.task_list = []
    def add_task(self,text):
        self.task_list.append(text)


if __name__ == '__main__':
    root = tk.Tk()
    manager = TaskManager()
    app = ToDoApp(root, manager)
    root.mainloop()
