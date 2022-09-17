#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import os
import json
from ... import project_runner

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
AUTO_START_APPS = ["transcript", "tutorial"]
CODE_TOOLS = ["transcript", "project_explorer"]
HELP_APPS = ["tutorial"]

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.setup_menu()

    def setup_menu(self):
        self.menubar = tk.Menu(self.mainwindow)

        code_tools = tk.Menu(self.menubar, tearoff=0)
        for code_tool in CODE_TOOLS:
            name = code_tool.replace("_", " ")
            name = name.title()
            code_tools.add_command(label=name, command=lambda: project_runner.run_project(f"core_apps/{code_tool}"))
        self.menubar.add_cascade(label="Code Tools", menu=code_tools)

        help_apps = tk.Menu(self.menubar, tearoff=0)
        for app in HELP_APPS:
            name = app.replace("_", " ")
            name = name.title()
            help_apps.add_command(label=name, command=lambda: project_runner.run_project(f"core_apps/{app}"))
        self.menubar.add_cascade(label="Help", menu=help_apps)

        self.mainwindow.config(menu=self.menubar)

    def run(self):
        for app in AUTO_START_APPS:
            project_runner.run_project(f"core_apps/{app}")
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
