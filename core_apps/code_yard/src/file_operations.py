import tkinter as tk
import tkinter.filedialog
import pathlib
from .file import File

def save_file(code_yard):
        if code_yard.selected_file == None:
            save_file_as(code_yard)
        else:
            file = open(code_yard.selected_file.path, "w")
            file.write(code_yard.edit_area.text.get("1.0", tk.END))
            file.close()
            code_yard.selected_file.has_unsaved_changes = False
            code_yard.edit_area.selected_file_label.configure(text=code_yard.selected_file.name)

def save_file_as(code_yard):
    path = tkinter.filedialog.asksaveasfilename()
    if len(path) == 0:
        return

    path = pathlib.Path(path)
    name = path.name
    code_yard.selected_file = File(path, name)
    code_yard.edit_area.selected_file_label.configure(text=name)
    save_file(code_yard)

def new_file(code_yard):
    code_yard.edit_area.clear()
    code_yard.selected_file = None

def open_file(code_yard):
    if code_yard.selected_file != None and code_yard.selected_file.has_unsaved_changes:
        answer = tkinter.messagebox.askokcancel("Question", f"File '{code_yard.selected_file.name}' has unsaved changes, proceed?")
        if answer != True:
            return

    path = tkinter.filedialog.askopenfilename()
    if len(path) == 0:
        return
    path = pathlib.Path(path)
    name = path.name
    code_yard.selected_file = File(name, path)
    code_yard.edit_area.clear()
    code_yard.edit_area.redraw(open(code_yard.selected_file.path, "r").read())
    code_yard.edit_area.selected_file_label.configure(text=name)