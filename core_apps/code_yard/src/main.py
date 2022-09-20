#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from ... import tkinter_themes

class CodeYard:
    def __init__(self, master=None):
        # build ui
        master.title("Code Yard")

        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", row="0", sticky="nsew")

        self.file_explorer = ttk.Frame(master)
        self.file_explorer.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.file_explorer.tree = ttk.Treeview(self.file_explorer, height=20)
        self.file_explorer.tree.grid(column=0, row=0, padx=5, pady=5, sticky="ns")

        self.edit_area = ttk.Frame(master)
        self.edit_area.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")
        self.edit_area.text = tk.Text(self.edit_area)
        self.edit_area.text.grid(column=0, row=0, sticky="nsew")

        # Main widget
        self.mainwindow = self.frame1

        tkinter_themes.setup_global_tkinter_theme(root)

        self.setup_top_menu()

    def setup_top_menu(self):
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.open_file)

    def open_file(self):
        pass

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeYard(root)
    app.run()
