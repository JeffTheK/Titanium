import tkinter as tk
import tkinter.ttk as ttk
import string
import subprocess

TYPABLE_CHARS = list(string.ascii_letters)
TYPABLE_CHARS.append(" ")
TYPABLE_CHARS.extend(list("123456789"))
TYPABLE_CHARS.extend(list("~!@#$%^&*()-=_+{};:'\"\\|/,.<>"))

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
        if command == "clear":
            self.delete(0, tk.END)
            self.new_line()
            return
        try:
            result = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            self.new_line(start=f'"{command}" not found')
            self.new_line()
            return

        result_text = result.stdout.decode('utf-8')
        if result_text.count("\n") > 0:
            for line in result_text.split("\n"):
                self.new_line(start="")
                self.append_to_current_line(line)
        else:
            self.new_line(start="")
            self.append_to_current_line(result.stdout.decode('utf-8'))
        self.new_line()
        self.yview(tk.END)

    def new_line(self, start="$ "):
        self.insert(tk.END, start)
        self.current_line_text = start

    def erase_current_line_char(self):
        if len(self.current_line_text) == 2:
            return

        self.current_line_text = self.current_line_text[:-1]
        self.delete(tk.END)
        self.insert(tk.END, self.current_line_text)

    def on_key_press(self, event):
        print(event)
        if event.char in TYPABLE_CHARS:
            self.append_to_current_line(event.char)