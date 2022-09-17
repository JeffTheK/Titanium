#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
import os
import json

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
AUTO_START_APPS = ["transcript"]

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)

    def run(self):
        for app in AUTO_START_APPS:
            self.run_project(f"core_apps/{app}")
        self.mainwindow.mainloop()

    def run_project(self, path):
        project_file = open(os.path.join(path, ".project.json"), "r")
        project_json = json.loads(project_file.read())
        run_command = project_json["run_command"]
        os.system(run_command)

    def on_open_transcript_button_clicked(self):
        self.run_project("core_apps/transcript")

    def on_open_project_explorer_button_clicked(self):
        self.run_project("core_apps/project_explorer")

if __name__ == "__main__":
    app = MainApp()
    app.run()
