#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from .popup_menu import PopupMenu
from .file_tree import FileTree

class ExampleApp:
    def __init__(self, master=None):
        self.frame1 = ttk.Frame(master)

        # build ui
        self.label1 = ttk.Label(master, text="right click me!")
        self.label1.popupmenu = PopupMenu(self.label1)
        self.label1.popupmenu.add_command(label="Option1", command=lambda: print("Option1"))
        self.label1.popupmenu.add_command(label="Option2", command=lambda: print("Option2"))
        self.label1.popupmenu.add_command(label="Option2", command=lambda: print("Option3"))
        self.label1.grid(row=0, column=0)

        self.file_tree = FileTree(master, "./")
        self.file_tree.grid(row=1, column=0)

        # Main widget
        self.mainwindow = self.frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    app.run()
