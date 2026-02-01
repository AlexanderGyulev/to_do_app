import tkinter as tk

class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("To Do App")
        self.root.geometry("600x600")