import tkinter as tk
import tkinter.ttk as ttk
from ... import code_actions_menu

class EditArea(ttk.Frame):
    def __init__(self, master, code_yard):
        ttk.Frame.__init__(self, master)
        self.code_yard = code_yard
        self.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")
        self.selected_file_label = ttk.Label(self, text="unnamed")
        self.selected_file_label.grid(column=0, row=0, pady=5, sticky="w")
        self.text = tk.Text(self)
        self.text.grid(column=0, row=1, sticky="nsew")
        self.text.bind("<Key>", lambda _: self.on_text_changed())
        self.text.code_actions_widget = code_actions_menu.CodeActionsWidget(self.text, self.text)
    
    def on_text_changed(self):
        if self.code_yard.selected_file != None:
            self.code_yard.selected_file.has_unsaved_changes = True
            self.selected_file_label.configure(text=str(self.code_yard.selected_file.name)+"*")
        
    def clear(self):
        self.text.delete("1.0", tk.END)

    def redraw(self, text):
        self.clear()
        self.text.insert("1.0", text)