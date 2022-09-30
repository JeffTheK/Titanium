#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import glob
from ... import tkinter_themes

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
SEARCH_LOCATION = PROJECT_PATH.parent.parent

class Finder:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.search_entry = builder.get_object("search_entry", master)
        self.search_path_entry = builder.get_object("search_path_entry")
        self.search_path_entry.insert("0", SEARCH_LOCATION)
        self.results_tree = builder.get_object("results_tree", master)
        builder.connect_callbacks(self)

        tkinter_themes.setup_global_tkinter_theme(self.mainwindow)

    def run(self):
        self.mainwindow.mainloop()

    def clear_results_tree(self):
        self.results_tree.delete(*self.results_tree.get_children())

    def search(self):
        found_items = []
        search_term = self.search_entry.get()
        search_location = self.search_path_entry.get()
        search_location = pathlib.Path(search_location)
        print(search_location)
        self.mainwindow.config(cursor="watch")
        self.mainwindow.update()
        found_items += search_location.rglob(f"*{search_term}*")
        self.clear_results_tree()
        for item in found_items:
            self.results_tree.insert("", tk.END, text=item, values=item)
        self.mainwindow.config(cursor="")

if __name__ == "__main__":
    app = Finder()
    app.run()
