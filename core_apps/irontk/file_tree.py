import imp
import tkinter as tk
import tkinter.ttk as ttk
import os
from . import default_settings

class FileTree(ttk.Treeview):
    def __init__(self, master, directory=None):
        ttk.Treeview.__init__(self, master)
        default_settings.setup(self)
        self.directory = directory
        if self.directory != None:
            self.redraw()

    def clear(self):
        self.delete(*self.get_children())

    def redraw(self):
        self.clear()
        self.walk_directory("", self.directory)

    def walk_directory(self, parent_dir, path):
        for item in os.listdir(path):
            item_full_path = os.path.join(path, item)
            self.insert("", "end", iid=item_full_path, values=(item, item_full_path), text=item, open=False)
            if parent_dir != "":
                self.move(item_full_path, path, "end")
            if os.path.isdir(item_full_path):
                self.walk_directory (path, item_full_path)