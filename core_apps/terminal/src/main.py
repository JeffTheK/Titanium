#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from ... import tk_term

class Terminal:
    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.pack(expand=True, fill=tk.BOTH)

        # Main widget
        self.mainwindow = self.frame1

        self.terminal = tk_term.Terminal(self.mainwindow)
        self.terminal.pack(expand=True, fill=tk.BOTH)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Terminal")
    app = Terminal(root)
    app.run()
