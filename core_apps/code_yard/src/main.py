#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import tkinter.messagebox
import pathlib
import os
from ... import tkinter_themes

class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.has_unsaved_changes = False

class CodeYard:
    def __init__(self, master=None):
        # build ui
        master.title("Code Yard")

        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", row="0", sticky="nsew")

        self.file_explorer = ttk.Frame(master)
        self.file_explorer.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.file_explorer.tree = ttk.Treeview(self.file_explorer, height=20)
        self.file_explorer.tree.grid(column=0, row=0, padx=5, pady=5, sticky="ns")
        self.file_explorer.tree.bind("<<TreeviewSelect>>", lambda _: self.on_file_explorer_item_select())

        self.edit_area = ttk.Frame(master)
        self.edit_area.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")
        self.edit_area.selected_file_label = ttk.Label(self.edit_area, text="unnamed")
        self.edit_area.selected_file_label.grid(column=0, row=0, pady=5, sticky="w")
        self.edit_area.text = tk.Text(self.edit_area)
        self.edit_area.text.grid(column=0, row=1, sticky="nsew")
        self.edit_area.text.bind("<Key>", lambda _: self.on_text_changed())

        self.selected_directory = os.getcwd()
        self.selected_file = None

        # Main widget
        self.mainwindow = self.frame1

        tkinter_themes.setup_global_tkinter_theme(root)

        self.setup_top_menu()
        self.redraw_file_explorer(self.selected_directory)

    def on_text_changed(self):
        if self.selected_file != None:
            self.selected_file.has_unsaved_changes = True
            self.edit_area.selected_file_label.configure(text=str(self.selected_file.name)+"*")

    def setup_top_menu(self):
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)

    def clear_edit_area(self):
        self.edit_area.text.delete("1.0", tk.END)

    def redraw_edit_area(self, text):
        self.clear_edit_area()
        self.edit_area.text.insert("1.0", text)

    def clear_file_explorer(self):
        self.file_explorer.tree.delete(*self.file_explorer.tree.get_children())

    def redraw_file_explorer(self, directory):
        self.clear_file_explorer()
        self.walk_directory("", directory)

    def walk_directory(self, parent_dir, path):
        for item in os.listdir(path):
            item_full_path = os.path.join(path, item)
            self.file_explorer.tree.insert("", "end", iid=item_full_path, values=(item, item_full_path), text=item, open=False)
            if parent_dir != "":
                self.file_explorer.tree.move(item_full_path, path, "end")
            if os.path.isdir(item_full_path):
                self.walk_directory (path, item_full_path)

    def save_file(self):
        if self.selected_file == None:
            self.save_file_as()
        else:
            file = open(self.selected_file.path, "w")
            file.write(self.edit_area.text.get("1.0", tk.END))
            file.close()
            self.selected_file.has_unsaved_changes = False
            self.edit_area.selected_file_label.configure(text=self.selected_file.name)

    def save_file_as(self):
        path = tkinter.filedialog.asksaveasfilename()
        if len(path) == 0:
            return

        path = pathlib.Path(path)
        name = path.name
        self.selected_file = File(path, name)
        self.edit_area.selected_file_label.configure(text=name)
        self.save_file()

    def new_file(self):
        self.clear_edit_area()
        self.selected_file = None

    def open_file(self):
        if self.selected_file != None and self.selected_file.has_unsaved_changes:
            answer = tkinter.messagebox.askokcancel("Question", f"File '{self.selected_file.name}' has unsaved changes, proceed?")
            if answer != True:
                return

        path = tkinter.filedialog.askopenfilename()
        if len(path) == 0:
            return
        path = pathlib.Path(path)
        name = path.name
        self.selected_file = File(name, path)
        self.clear_edit_area()
        self.redraw_edit_area(open(self.selected_file.path, "r").read())
        self.edit_area.selected_file_label.configure(text=name)

    def on_close_window(self):
        if self.selected_file != None and self.selected_file.has_unsaved_changes:
            answer = tkinter.messagebox.askokcancel("Question", f"File '{self.selected_file.name}' has unsaved changes, proceed?")
            if answer != True:
                return
        root.destroy()

    def run(self):
        self.mainwindow.mainloop()

    def on_file_explorer_item_select(self):
        selected_item = self.file_explorer.tree.selection()[0]
        selected_item = self.file_explorer.tree.item(selected_item, "values")
        selected_item = File(selected_item[0], selected_item[1])

        if os.path.isdir(selected_item.path):
            return
        if self.selected_file != None and self.selected_file.has_unsaved_changes:
            answer = tkinter.messagebox.askokcancel("Question", f"File '{self.selected_file.name}' has unsaved changes, proceed?")
            if answer != True:
                return

        self.selected_file = selected_item
        self.edit_area.selected_file_label.configure(text=self.selected_file.name)
        self.clear_edit_area()
        file = open(self.selected_file.path, "r")
        text = file.read()
        file.close()
        self.edit_area.text.insert("1.0", text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeYard(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close_window)
    app.run()
