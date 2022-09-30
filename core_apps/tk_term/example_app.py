#!/usr/bin/python3
from symbol import term
import tkinter as tk
import tkinter.ttk as ttk
from . import terminal

class ExampleApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", row="0")

        # Main widget
        self.mainwindow = self.frame1

        self.terminal = terminal.Terminal(self.mainwindow)
        self.terminal.pack()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    app.run()
