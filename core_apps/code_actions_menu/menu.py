import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import sys
from pathlib import Path
from .. import code_runner
from .. import irontk

class CodeActionsWidget:
    def __init__(self, master, edit_area_text):
        master.code_actions_widget = self
        self.selected_language = "python"
        self.edit_area_text = edit_area_text
        irontk.popup_menu.setup(self.edit_area_text)
        self.do_it_image = tk.PhotoImage(file=Path( __file__ ).parent / "do_it.png")
        self.edit_area_text.popup_menu.add_command(label=" Do It", command=self.on_do_it_pressed, image=self.do_it_image, compound="left")

    def on_do_it_pressed(self):
        code = self.edit_area_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        output, out_text = code_runner.run_code(code, self.selected_language)
        self.edit_area_text.insert("end", out_text)
        if output != None:
            self.edit_area_text.insert("end", str(output))

def setup(master, edit_area_text):
    widget = CodeActionsWidget(master, edit_area_text)