import imp
import tkinter as tk
import tkinter.ttk as ttk
import string
import subprocess

from numpy import append

class Terminal(tk.Listbox):
    def __init__(self, master):
        tk.Listbox.__init__(self, master)
        self.current_line_text = ""
        self.append_to_current_line("$ ")
        self.bind("<Key>", self.on_key_press)
        self.bind("<BackSpace>", lambda _: self.erase_current_line_char())
        self.bind("<Return>", lambda _: self.execute_current_line())
        self.configure(width=80, height=24)

    def append_to_current_line(self, element):
        self.current_line_text += element
        self.delete(tk.END)
        self.insert(tk.END, self.current_line_text)

    def execute_current_line(self):
        self.current_line_text
        command = self.current_line_text[2:]
        try:
            result = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            self.new_line(start=f'"{command}" not found')
            self.new_line()
            return

        self.new_line(start="")
        self.append_to_current_line(result.stdout.decode('utf-8').replace("\n", " "))
        self.new_line()

    def new_line(self, start="$ "):
        self.insert(tk.END, start)
        self.current_line_text = start

    def erase_current_line_char(self):
        if len(self.current_line_text) == 2:
            return

        self.current_line_text = self.current_line_text[:-1]
        self.delete(tk.END)
        self.insert(tk.END, self.current_line_text)

    def on_enter(self):
        pass

    def on_key_press(self, event):
        print(event)
        if event.char in string.ascii_letters:
            char = event.char
            if char in string.ascii_letters:
                self.append_to_current_line(char)