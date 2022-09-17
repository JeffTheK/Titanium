#!/usr/bin/python3
from distutils.command.build import build
import pathlib
import tkinter.ttk as ttk
import pygubu
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
SUPPORTED_LANGUAGES = ["python"]
NEW_PROJECT_PATH = PROJECT_PATH.parent.parent

PROJECT_JSON_FILE_TEMPLATE = """ {
    "run_command": "python3 -m core_apps.PROJECT_NAME.src.main"
}
"""

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.project_name_entry = builder.get_object("project_name_entry", master)

        self.__tkvar = None
        builder.import_variables(self, ["__tkvar"])

        builder.connect_callbacks(self)

    def on_language_selected(self, selection):
        self.selected_language = selection.lower()

    def create_project(self):
        project_name = self.project_name_entry.get()
        project_path = NEW_PROJECT_PATH / project_name
        os.mkdir(project_path)
        os.mkdir(project_path / "src")
        self.create_project_json_file(project_name, project_path)
        self.mainwindow.destroy()

    def create_project_json_file(self, project_name, project_path):
        project_json_file = open(os.path.join(project_path, ".project.json"), "w")
        project_json_file.write(PROJECT_JSON_FILE_TEMPLATE.replace("PROJECT_NAME", project_name))
        project_json_file.close()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
