#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
PROJECTS_DIRS = ["../../"]

class Project:
    def __init__(self, name, path):
        self.name = name
        self.path = path

class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.project_tree = builder.get_object("project_tree", master)
        self.project_tree.heading("#0", text="Projects")
        self.file_tree = builder.get_object("file_tree", master)
        self.file_tree.heading("#0", text="Files")
        self.edit_area = builder.get_object("edit_area", master)
        self.edit_area.text = builder.get_object("text", self.edit_area)
        self.selected_project = None
        builder.connect_callbacks(self)
        self.load_projects()

    def run(self):
        self.mainwindow.mainloop()

    def clear_file_tree(self):
        for i in self.file_tree.get_children():
            self.file_tree.delete(i)

    def on_project_select(self, event=None):
        selected_item = self.project_tree.selection()[0]
        self.selected_project = self.project_tree.item(selected_item, "values")
        self.selected_project = Project(self.selected_project[0], self.selected_project[1])
        files = os.listdir(self.selected_project.path)
        self.clear_file_tree()
        self.load_project_directory("", self.selected_project.path)

    def on_file_select(self, event=None):
        selected_item = self.file_tree.selection()[0]
        self.selected_file = self.file_tree.item(selected_item, "values")
        self.selected_file = File(self.selected_file[0], self.selected_file[1])
        if not os.path.isfile(self.selected_file.path):
            return
        file = open(self.selected_file.path)
        try:
            text = file.read()
        except UnicodeDecodeError:
            return
        self.edit_area.text.delete('1.0', "end")
        self.edit_area.text.insert("1.0", text)

    def load_projects(self):
        for project_dir in PROJECTS_DIRS:
            for dir in os.listdir(project_dir):
                self.load_project(os.path.join(project_dir, dir))

    def load_project(self, path):
        name = os.path.basename(path)
        self.project_tree.insert("", "end", values=(name, path), text=name)

    def load_project_directory(self, parent_dir, path):
        for item in os.listdir(path):
            item_full_path = os.path.join(path, item)
            self.file_tree.insert("", "end", iid=item_full_path, values=(item, item_full_path), text=item, open=True)
            if parent_dir != "":
                self.file_tree.move(item_full_path, path, "end")
            if os.path.isdir(item_full_path):
                self.load_project_directory(path, item_full_path)

if __name__ == "__main__":
    app = MainApp()
    app.run()
