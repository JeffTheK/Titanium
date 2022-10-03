#!/usr/bin/python3

import tkinter as tk
from tkhtmlview import HTMLText
from .. import tk_syntax_highlight

root = tk.Tk()
text = tk.Text(root)
text.bind("<KeyRelease>", lambda _: tk_syntax_highlight.highlight(text.get("1.0", tk.END), "python", text))
text.pack()

tk.mainloop()