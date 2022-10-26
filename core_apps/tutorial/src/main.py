#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from ... import tkinter_themes
from tkfontawesome import icon_to_image

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
PAGES_PATH = PROJECT_PATH.parent / "pages"

class MainApp:
    """An app with tutorial pages you can browse"""
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.page_tree = builder.get_object("page_tree", master)
        self.page_tree.heading("#0", text="Pages")
        self.text = builder.get_object("text", master)
        self.page_icon = icon_to_image("file-alt", scale_to_height=16)
        self.selected_page = None
        builder.connect_callbacks(self)
        self.setup_pages()
        children = self.page_tree.get_children()
        if children:
            self.page_tree.focus(children[0])
            self.page_tree.selection_set(children[0])

        tkinter_themes.setup_global_tkinter_theme(self.mainwindow)

    def run(self):
        """Runs the app"""
        self.mainwindow.mainloop()

    def setup_pages(self):
        """Puts pages into page tree from folder"""
        for page in PAGES_PATH.iterdir():
            self.page_tree.insert('', tk.END, values=str(page.absolute()), text=" " + page.name,
                image=self.page_icon)
        self.page_tree.focus_set()

    def on_page_select(self, _event=None):
        """When page is selected show text from the new page"""
        selected_item = self.page_tree.selection()[0]
        self.selected_page = self.page_tree.item(selected_item, "values")
        path = self.selected_page[0]
        page_file = open(path, "r", encoding="utf8")
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', page_file.read())
        page_file.close()

if __name__ == "__main__":
    app = MainApp()
    app.run()
