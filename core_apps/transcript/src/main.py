#!/usr/bin/python3
import code
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import sys
from ... import code_actions_menu
from ... import code_runner
from ... import tkinter_themes
from ... import tk_syntax_highlight
from . import cli

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
        self.language_option = builder.get_object("language_option", master)
        self.do_it_button = builder.get_object("do_it_button", master)
        builder.connect_callbacks(self)

        code_actions_menu.setup(self.edit_area.text, self.edit_area.text)
        self.do_it_button.config(image=self.edit_area.text.code_actions_widget.do_it_icon)
        self.edit_area.text.bind("<KeyRelease>", lambda _: tk_syntax_highlight.highlight(self.edit_area.text.get("1.0", tk.END), self.selected_language, self.edit_area.text))
        self.selected_language = "python"

        tkinter_themes.setup_global_tkinter_theme(self.mainwindow)

    def on_do_it_pressed(self):
        code = self.edit_area.text.get('1.0', tk.END)
        output, out_text = code_runner.run_code(code, self.selected_language)
        self.edit_area.text.insert(tk.END, out_text)

    def on_language_selected(self, selection):
        self.selected_language = selection.lower()
        self.edit_area.text.code_actions_widget.language = self.selected_language

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = Transcript()
    if len(sys.argv) > 1:
        cli.cli(sys.argv, app)
    app.run()
