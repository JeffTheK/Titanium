import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky="nesw")