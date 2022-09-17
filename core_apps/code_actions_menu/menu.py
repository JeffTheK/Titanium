import tkinter.ttk as ttk
import tkinter as tk
import pygubu
import sys
from .. import code_runner

class CodeActionsWidget:
    def __init__(self, master, edit_area_text):
        master.code_actions_widget = self
        self.edit_area_text = edit_area_text
        self.popup_menu = tk.Menu(master, tearoff=0)
        self.popup_menu.add_command(label="Do It", command=self.on_do_it_pressed)
        self.edit_area_text.bind("<Button-3>", self.popup_right_click_menu) # Button-2 on Aqua

    def on_do_it_pressed(self):
        code = self.edit_area_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        output, out_text = code_runner.run_code(code, "python")
        self.edit_area_text.insert("end", out_text)
        if output != None:
            self.edit_area_text.insert("end", str(output))

    def popup_right_click_menu(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

def setup(master, edit_area_text):
    widget = CodeActionsWidget(master, edit_area_text)