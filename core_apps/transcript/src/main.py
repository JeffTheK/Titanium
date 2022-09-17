#!/usr/bin/python3
import code
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import sys
from ... import code_actions_menu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"


class Transcript:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.edit_area = builder.get_object("edit_area")
        self.edit_area.text = builder.get_object("text", self.edit_area)
        builder.connect_callbacks(self)

        code_actions_menu.setup(self.mainwindow, self.edit_area.text)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = Transcript()
    app.run()
