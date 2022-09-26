#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import tkinter.messagebox
import os
from ... import tkinter_themes
from . import edit_area
from . import file_explorer
from . import menubar

class CodeYard:
    def __init__(self, master=None):
        # build ui
        master.title("Code Yard")

        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", row="0", sticky="nsew")

        self.file_explorer = file_explorer.FileExplorer(master, self)

        self.edit_area = edit_area.EditArea(master, self)

        self.selected_directory = os.getcwd()
        self.selected_file = None

        # Main widget
        self.mainwindow = self.frame1

        tkinter_themes.setup_global_tkinter_theme(root)

        self.menubar = menubar.Menubar(root, self)
        self.file_explorer.redraw(self.selected_directory)

    def on_close_window(self):
        if self.selected_file != None and self.selected_file.has_unsaved_changes:
            answer = tkinter.messagebox.askokcancel("Question", f"File '{self.selected_file.name}' has unsaved changes, proceed?")
            if answer != True:
                return
        root.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeYard(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close_window)
    app.run()
