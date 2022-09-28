#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import os
from ... import code_actions_menu
from ... import project_runner
from ... import irontk
from ... import code_runner
from ... import tkinter_themes

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"
PROJECT_CREATOR_PATH = PROJECT_PATH.parent.parent / "project_creator"
PROJECT_RUNNER_PATH = PROJECT_PATH.parent.parent / "project_runner"
PROJECTS_DIRS = ["core_apps"]

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
        code_actions_menu.setup(self.mainwindow, self.edit_area.text)

        self.project_tree.popup_menu = irontk.popup_menu.PopupMenu(self.project_tree)
        self.project_tree.popup_menu.add_command(label="Run Project", command=lambda: project_runner.run_project(self.selected_project.path))
        self.project_tree.popup_menu.add_command(label="New Project", command=lambda: project_runner.run_project(PROJECT_CREATOR_PATH))

        self.file_tree.popup_menu = irontk.popup_menu.PopupMenu(self.file_tree)
        self.file_tree.popup_menu.add_command(label="New File", command=lambda: self.new_file())
        self.file_tree.popup_menu.add_command(label="Rename File", command=lambda: self.rename_file())
        self.file_tree.popup_menu.add_command(label="Run File", command=lambda: self.run_file())

        self.edit_area.text.bind('<Control-s>', lambda _: self.save_file())
        self.file_tree.bind('<F2>', lambda _: self.rename_file())
        self.project_tree.bind('<Control-r>', lambda _: self.run_project())
        self.project_tree.bind('<Control-n>', lambda _: project_runner.run_project(PROJECT_CREATOR_PATH))

        tkinter_themes.setup_global_tkinter_theme(self.mainwindow)

    def run(self):
        self.mainwindow.mainloop()

    def new_file(self):
        path = pathlib.Path(self.selected_file.path).parent / "new_file.py"
        name = "new_file.py"
        file = open(path, "w")
        self.redraw_file_tree()
        file.close()

    def rename_file(self):
        self.file_tree.bind("<KeyPress>", self.on_file_rename)

    def on_file_rename(self, event):
        selected_item = self.file_tree.selection()[0]
        print(event.keysym)
        if event.keysym == "BackSpace":
            new_name = self.selected_file.name[:-1]
            self.file_tree.item(selected_item, text=new_name)
            self.selected_file.name = new_name
        elif event.keysym == "Return":
            self.file_tree.unbind("<KeyPress>")
            new_path = pathlib.Path(self.selected_file.path).parent / self.selected_file.name
            os.rename(self.selected_file.path, new_path)
        elif event.keysym == "Escape":
            self.file_tree.unbind("<KeyPress>")
            self.redraw_file_tree()
        else:
            new_name = self.selected_file.name + event.char
            self.file_tree.item(selected_item, text=new_name)
            self.selected_file.name = new_name

    def run_file(self):
        file = open(self.selected_file.path, "r")
        output, out_text = code_runner.run_code(file.read(), "python")
        self.edit_area.text.delete('1.0', tk.END)
        self.edit_area.text.insert('1.0', out_text)
        file.close()

    def clear_file_tree(self):
        for i in self.file_tree.get_children():
            self.file_tree.delete(i)

    def redraw_file_tree(self):
        self.clear_file_tree()
        self.load_project_directory("", self.selected_project.path)

    def run_project(self):
        if self.selected_project == None:
            return
        project_runner.run_project(self.selected_project.path)

    def save_file(self):
        if self.selected_file == None:
            return
        new_text = self.edit_area.text.get('1.0', tk.END)
        file = open(self.selected_file.path, "w")
        file.write(new_text)
        file.close()

    def on_project_select(self, event=None):
        selected_item = self.project_tree.selection()[0]
        self.selected_project = self.project_tree.item(selected_item, "values")
        self.selected_project = Project(self.selected_project[0], self.selected_project[1])
        files = os.listdir(self.selected_project.path)
        self.redraw_file_tree()

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
