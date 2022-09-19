#!/usr/bin/python3
from importlib.resources import path
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import os
import pathlib
import platform

OUTPUT_DIR_PATH = pathlib.Path.home()
DEFAULT_SCREENSHOT_NAME = "screenshot" + datetime.now().strftime("_%d_%m_%y")

class Screenshot:
    def __init__(self, master=None):
        # build ui
        master.title("Screenshot")
        master.geometry("400x200")
        self.main_frame = ttk.Frame(master)
        self.main_frame.configure(height="300", width="200")
        self.main_frame.grid(column="0", row="0", sticky="nsew")
        self.main_frame.rowconfigure("0", weight="1")
        self.main_frame.columnconfigure("0", weight="1")
        self.main_frame.rowconfigure("1", weight="1")
        self.main_frame.columnconfigure("1", weight="1")

        self.output_path_label = ttk.Label(self.main_frame)
        self.output_path_label.configure(text="Output Path:")
        self.output_path_label.grid(column=0, row=0, padx=5, pady=5, sticky="e")

        self.output_path_entry = ttk.Entry(self.main_frame)
        self.output_path_entry.configure()
        self.output_path_entry.insert(0, str(OUTPUT_DIR_PATH / DEFAULT_SCREENSHOT_NAME))
        self.output_path_entry.grid(column=1, row=0, padx=5, pady=5, sticky="ew")

        # buttons
        self.screenshot_button = ttk.Button(self.main_frame)
        self.screenshot_button.configure(text="Take Screenshot", command=self.take_whole_screen_screenshot)
        self.screenshot_button.grid(column="0", row="1", columnspan="2", padx=5, pady=5)

        # Main widget
        self.main_window = self.main_frame
        master.rowconfigure("0", weight="1")
        master.columnconfigure("0", weight="1")

    def take_whole_screen_screenshot(self):
        if platform.system() == "Windows" or platform.system() == "Darwin":
            from PIL import ImageGrab
            image = ImageGrab.grab()
            image.save(str(OUTPUT_DIR_PATH / DEFAULT_SCREENSHOT_NAME) + ".png")
        else:
            import pyautogui
            image = pyautogui.screenshot()
            image.save(str(OUTPUT_DIR_PATH / DEFAULT_SCREENSHOT_NAME) + ".png")

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Screenshot(root)
    app.run()
