from genericpath import isfile
import tkinter as tk
import tkinter.ttk as ttk
import os
import tkinter.messagebox
from .file import File
from tkfontawesome import icon_to_image

class FileExplorer(ttk.Frame):
    def __init__(self, master, code_yard):
        ttk.Frame.__init__(self, master)
        self.code_yard = code_yard
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.tree = ttk.Treeview(self, height=20)
        self.tree.grid(column=0, row=0, padx=5, pady=5, sticky="ns")
        self.tree.bind("<<TreeviewSelect>>", lambda _: self.on_tree_item_select())
        self.file_icon = icon_to_image("file", scale_to_height=16, fill="#1D9F75")
        self.folder_icon = icon_to_image("folder", scale_to_height=16, fill="#ebab34")

    def clear(self):
        self.tree.delete(*self.tree.get_children())

    def redraw(self, directory):
        self.clear()
        self.tree.heading("#0", text=directory)
        self.walk_directory("", directory)

    def walk_directory(self, parent_dir, path):
        for item in os.listdir(path):
            item_full_path = os.path.join(path, item)
            if os.path.isfile(item_full_path):
                self.tree.insert("", "end", iid=item_full_path, values=(item, item_full_path), text=" " + str(item), open=False, image=self.file_icon)
            else:
                self.tree.insert("", "end", iid=item_full_path, values=(item, item_full_path), text=" " + str(item), open=False, image=self.folder_icon)
            if parent_dir != "":
                self.tree.move(item_full_path, path, "end")
            if os.path.isdir(item_full_path):
                self.walk_directory (path, item_full_path)
    
    def on_tree_item_select(self):
        selected_item = self.tree.selection()[0]
        selected_item = self.tree.item(selected_item, "values")
        selected_item = File(selected_item[0], selected_item[1])

        if os.path.isdir(selected_item.path):
            return
        if self.code_yard.selected_file != None and self.code_yard.selected_file.has_unsaved_changes:
            answer = tkinter.messagebox.askokcancel("Question", f"File '{self.code_yard.selected_file.name}' has unsaved changes, proceed?")
            if answer != True:
                return

        self.code_yard.selected_file = selected_item
        self.code_yard.edit_area.selected_file_label.configure(text=self.code_yard.selected_file.name)
        self.code_yard.edit_area.clear()
        file = open(self.code_yard.selected_file.path, "r")
        text = file.read()
        file.close()
        self.code_yard.edit_area.redraw(text)