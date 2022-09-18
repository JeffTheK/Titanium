#!/usr/bin/python3
import code
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import sys
from ... import code_actions_menu
from ... import code_runner

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

    def on_do_it_pressed(self):
        code = self.edit_area.text.get('1.0', tk.END)
        output, out_text = code_runner.run_code(code, self.selected_language)
        self.edit_area.text.insert(tk.END, out_text)

    def on_language_selected(self, selection):
        self.selected_language = selection.lower()
        self.mainwindow.code_actions_widget.language = self.selected_language

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = Transcript()
    app.run()
