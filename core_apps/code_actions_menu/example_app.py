#!/usr/bin/python3

import tkinter as tk
from .. import code_actions_menu

root = tk.Tk()
text = tk.Text(root)
text.pack()
text.code_actions_widget = code_actions_menu.CodeActionsWidget(text, text)

tk.mainloop()