#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
import sys

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"


class Transcript:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)
        self.edit_area = builder.get_object("edit_area")
        self.edit_area.text = builder.get_object("text", self.edit_area)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_do_it_pressed(self):
        original_stdout_write = sys.stdout.write
        original_stderr_write = sys.stderr.write
        sys.stdout.write = self.stdout_write_redirector
        sys.stderr.write = self.stdout_write_redirector

        code = self.edit_area.text.get("1.0","end-1c")
        output = exec(code)
        if output != None:
            self.edit_area.text.insert("end", str(output))

        sys.stdout.write = original_stdout_write
        sys.stderr.write = original_stderr_write

    def stdout_write_redirector(self, input_str):
        self.edit_area.text.insert("end", input_str)

if __name__ == "__main__":
    app = Transcript()
    app.run()
