#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
PAGES_PATH = PROJECT_PATH.parent / "pages"

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.page_tree = builder.get_object("page_tree", master)
        self.text = builder.get_object("text", master)
        builder.connect_callbacks(self)
        self.setup_pages()

    def run(self):
        self.mainwindow.mainloop()

    def setup_pages(self):
        for page in PAGES_PATH.iterdir():
            self.page_tree.insert('', tk.END, values=str(page.absolute()), text=page.name)
        self.page_tree.focus_set()

    def on_page_select(self, event=None):
        selected_item = self.page_tree.selection()[0]
        self.selected_page = self.page_tree.item(selected_item, "values")
        path = self.selected_page[0]
        page_file = open(path, "r")
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', page_file.read())
        page_file.close()

if __name__ == "__main__":
    app = MainApp()
    app.run()
