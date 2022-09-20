#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import json
import pathlib
import os
from ... import tkinter_themes
from ... import project_runner

SETTINGS_FILES_DIR = pathlib.Path.home() / ".titanium"

class Settings:
    def __init__(self, master=None):
        # build ui
        master.title("Settings")
        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", row="0")

        # Main widget
        self.mainwindow = self.frame1
        tkinter_themes.setup_global_tkinter_theme(root)

        self.setup_settings()

    def setup_settings(self):
        i = 0
        for file in os.listdir(SETTINGS_FILES_DIR):
            self.label_frame = ttk.LabelFrame(self.mainwindow, text=file)
            self.label_frame.configure(height=200, width=200)
            self.label_frame.grid(column=0, row=i, padx=5, pady=5, ipadx=5, ipady=5)
            file_path = SETTINGS_FILES_DIR / file
            text = open(file_path, "r").read()
            json_data = json.loads(text)
            i += 1
            j = 0
            for key, item in json_data.items():
                if type(item) == list:
                    self.label_frame.list_item_label = ttk.Label(self.label_frame, text=key + ":")
                    self.label_frame.list_item_label.grid(column=0, row=j, padx=5, pady=5)
                    self.label_frame.list_item_entry = ttk.Entry(self.label_frame)
                    self.label_frame.list_item_entry.insert(0, str(item).replace("'", '"'))
                    self.label_frame.list_item_entry.grid(column=1, row=j, padx=5, pady=5)
                self.label_frame.edit_file_button = ttk.Button(self.label_frame, text="Edit File")
                self.label_frame.edit_file_button.grid(column=0, row=j+1, padx=5, pady=5)
                j += 1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Settings(root)
    app.run()
