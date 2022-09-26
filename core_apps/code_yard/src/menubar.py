import tkinter as tk
from . import file_operations

class Menubar(tk.Menu):
    def __init__(self, master, code_yard):
        tk.Menu.__init__(self, master)
        master.config(menu=self)

        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", command=lambda: file_operations.new_file(code_yard))
        file_menu.add_command(label="Open File", command=lambda: file_operations.open_file(code_yard))
        file_menu.add_command(label="Save File", command=lambda: file_operations.save_file(code_yard))