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

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.setup_menu()

    def exe_exists(self, name):
        from shutil import which
        return which(name) is not None

    def setup_menu(self):
        self.menubar = tk.Menu(self.mainwindow)

        code_tools = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Code Tools", menu=code_tools)
        code_tools.add_command(label="Transcript", command=lambda: project_runner.run_project("core_apps/transcript"))
        code_tools.add_command(label="Project Explorer", command=lambda: project_runner.run_project("core_apps/project_explorer"))
        code_tools_other = tk.Menu(code_tools, tearoff=0)
        code_tools_other.add_command(label="Project Creator", command=lambda: project_runner.run_project("core_apps/project_creator"))
        code_tools.add_cascade(label="Other", menu=code_tools_other)

        system_apps = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="System", menu=system_apps)
        system_apps.add_command(label="Finder", command=lambda: project_runner.run_project("core_apps/finder"))
        system_apps.add_command(label="Screenshot", command=lambda: project_runner.run_project("core_apps/screenshot"))

        help_apps = tk.Menu(self.menubar, tearoff=0)
        help_apps.add_command(label="Tutorial", command=lambda: project_runner.run_project("core_apps/tutorial"))
        if (self.exe_exists("zeal")):
            help_apps.add_command(label="Zeal", command=lambda: os.system("zeal"))
        else:
            help_apps.add_command(label="Zeal", command=lambda: os.system("zeal"), state=tk.DISABLED)
        self.menubar.add_cascade(label="Help", menu=help_apps)

        other_apps = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Other", menu=other_apps)
        other_apps.add_command(label="Zen Installer", command=lambda: project_runner.run_project("core_apps/zen_installer"))

        self.mainwindow.config(menu=self.menubar)

    def run(self):
        for app in AUTO_START_APPS:
            project_runner.run_project(f"core_apps/{app}")
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
