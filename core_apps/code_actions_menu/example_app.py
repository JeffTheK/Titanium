#!/usr/bin/python3

import tkinter as tk
import menu

root = tk.Tk()
text = tk.Text(root)
text.pack()
menu.setup(root, text)

tk.mainloop()