#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class ZenInstaller:
    def __init__(self, master=None):
        # build ui
        master.title("Zen Installer")
        self.main_frame = ttk.Frame(master)
        self.main_frame.configure(height="200", width="200")
        self.main_frame.grid(column="0", row="0")

        # buttons
        self.zeal_button = ttk.Button(self.main_frame)
        self.zeal_button.configure(text="Install Zeal", command=self.install_zeal)
        self.zeal_button.grid(column="0", row="0")

        # Main widget
        self.main_window = self.main_frame

    def install_zeal(self):
        webbrowser.open("https://zealdocs.org/")

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ZenInstaller(root)
    app.run()
