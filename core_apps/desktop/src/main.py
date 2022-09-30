#!/usr/bin/python3
import pathlib
from tkinter.tix import AUTO
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import os
import json
from ... import project_runner
from ... import tkinter_themes

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
SETTINGS_FILES_DIR = pathlib.Path.home() / ".titanium"
SETTINGS_FILE_PATH = SETTINGS_FILES_DIR / "desktop.json"
AUTO_START_APPS = ["transcript", "tutorial"]

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.setup_menu()
        self.load_settings()

    def load_settings(self):
        if not os.path.exists(SETTINGS_FILES_DIR):
            os.mkdir(SETTINGS_FILES_DIR)
        if not os.path.exists(SETTINGS_FILE_PATH):
            from . import default_settings
            file = open(SETTINGS_FILE_PATH, "w")
            file.write(default_settings.DEFAULT_SETTINGS_TEXT)
            file.close()
        file = SETTINGS_FILE_PATH.open("r")
        text = file.read()
        if text == "":
            from . import default_settings
            file.write(default_settings.DEFAULT_SETTINGS_TEXT)
            text = file.read()
        
        global AUTO_START_APPS
        json_data = json.loads(text)
        AUTO_START_APPS = json_data["auto_start_apps"]

        file.close()

    def exe_exists(self, name):
        from shutil import which
        return which(name) is not None

    def setup_menu(self):
        self.menubar = tk.Menu(self.mainwindow)

        titanium_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Titanium", menu=titanium_menu)
        titanium_menu.add_command(label="Settings", command=lambda: project_runner.run_project("core_apps/settings"))

        code_tools = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Code Tools", menu=code_tools)
        code_tools.add_command(label="Transcript", command=lambda: project_runner.run_project("core_apps/transcript"))
        code_tools.add_command(label="Project Explorer", command=lambda: project_runner.run_project("core_apps/project_explorer"))
        code_tools.add_command(label="Code Yard", command=lambda: project_runner.run_project("core_apps/code_yard"))
        code_tools_other = tk.Menu(code_tools, tearoff=0)
        code_tools_other.add_command(label="Project Creator", command=lambda: project_runner.run_project("core_apps/project_creator"))
        code_tools.add_cascade(label="Other", menu=code_tools_other)

        system_apps = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="System", menu=system_apps)
        system_apps.add_command(label="Terminal", command=lambda: project_runner.run_project("core_apps/terminal"))
        system_apps.add_command(label="Finder", command=lambda: project_runner.run_project("core_apps/finder"))
        system_apps.add_command(label="Screenshot", command=lambda: project_runner.run_project("core_apps/screenshot"))
        system_apps.add_command(label="Screen Recorder", command=lambda: project_runner.run_project("core_apps/screen_recorder"))

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
        tkinter_themes.setup_global_tkinter_theme(self.mainwindow)

    def run(self):
        for app in AUTO_START_APPS:
            project_runner.run_project(f"core_apps/{app}")
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
