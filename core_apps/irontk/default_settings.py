import tkinter as tk
import tkinter.ttk as ttk

PADX = 5
PADY = 5
STICKY = "nesw"

def setup(master):
    master.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=STICKY)