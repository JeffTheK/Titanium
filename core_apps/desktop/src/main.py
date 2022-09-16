#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
import os

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
            os.system(f"cd core_apps/{app}/src/ && python3 main.py &")
        self.mainwindow.mainloop()

    def on_open_transcript_button_clicked(self):
        os.system("cd core_apps/transcript/src/ && python3 main.py")

if __name__ == "__main__":
    app = MainApp()
    app.run()
