import tkinter.ttk as ttk
import tkinter as tk
from black import out
import pygubu
import sys
from pathlib import Path
from .. import code_runner
from .. import irontk
from .. import project_runner
from tkfontawesome import icon_to_image

class CodeActionsWidget:
    def __init__(self, master, edit_area_text):
        master.code_actions_widget = self
        self.language = "python"
        self.do_it_icon = icon_to_image("play", scale_to_height=16, fill="#32a852")
        self.edit_area_text = edit_area_text
        self.edit_area_text.popup_menu = irontk.PopupMenu(self.edit_area_text)
        self.edit_area_text.popup_menu.add_command(label=" Do It", command=self.on_do_it_pressed, image=self.do_it_icon, compound="left")
        self.edit_area_text.popup_menu.add_command(label=" Do It in New Window", command=self.do_it_in_new_window, image=self.do_it_icon, compound="left")

    def on_do_it_pressed(self):
        code = self.edit_area_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        output, out_text = code_runner.run_code(code, self.language)
        self.edit_area_text.insert("end", out_text)
        if output != None:
            self.edit_area_text.insert("end", str(output))

    def do_it_in_new_window(self):
        code = self.edit_area_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        output, out_text = code_runner.run_code(code, self.language)
        if output != None:
            project_runner.run_project("core_apps/transcript", f"-text \"{out_text} {output}\"")
        else:
            project_runner.run_project("core_apps/transcript", f"-text \"{out_text}\"")

def setup(master, edit_area_text):
    widget = CodeActionsWidget(master, edit_area_text)