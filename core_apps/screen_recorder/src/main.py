#!/usr/bin/python3
from importlib.resources import is_resource
import tkinter as tk
import tkinter.ttk as ttk
import datetime
import pathlib
import cv2
import numpy as np
import pyautogui

DEFAULT_OUTPUT_DIR_PATH = pathlib.Path.home()
DEFAULT_RECORDING_NAME = "recording" + datetime.datetime.now().strftime("_%d_%m_%y")

class ScreenRecorder:
    def __init__(self, master=None):
        # build ui
        self.root = master
        master.title("Screen Recorder")
        self.frame = ttk.Frame(master)

        self.output_path_label = ttk.Label(self.frame)
        self.output_path_label.configure(text="Output Path")
        self.output_path_label.grid(column="0", row="0", padx=5, pady=5)

        self.output_path_entry = ttk.Entry(self.frame)
        self.output_path_entry.configure()
        self.output_path_entry.insert(0, str(DEFAULT_OUTPUT_DIR_PATH / DEFAULT_RECORDING_NAME) + ".avi")
        self.output_path_entry.grid(column="1", row="0", padx=5, pady=5)

        self.timer_label = ttk.Label(self.frame)
        self.timer_label.configure(text="Recording Time: 0:00:00")
        self.timer_label.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        self.recording_button = ttk.Button(self.frame)
        self.recording_button.configure(text="Start Recording", command=self.start_recording)
        self.recording_button.grid(column="0", columnspan="2", row="2", padx=5, pady=5)

        self.frame.configure(height="200", width="200")
        self.frame.grid(column="0", row="0", sticky="nsew")

        # Main widget
        self.main_window = self.frame

        self.is_recording = False
        self.timer_seconds = 0
        self.resolution = (1920, 1080)
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.fps = 16

        self.update_timer()

    def update_timer(self):
        if self.is_recording:
            self.timer_seconds += 1
            self.timer_label.configure(text="Recording Time: " + str(datetime.timedelta(seconds=self.timer_seconds)))
        self.root.after(1000, self.update_timer)

    def frame_taking_loop(self):
        if not self.is_recording:
            return
        img = pyautogui.screenshot()
        frame = np.array(img)
        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.video_writer.write(frame)
        cv2.imshow('Live', frame)
        cv2.waitKey(1)
        self.root.after(1, self.frame_taking_loop)

    def start_recording(self):
        self.is_recording = True
        self.recording_button.configure(text= "Stop Recording", command=self.stop_recording)
        self.output_file_name = self.output_path_entry.get()
        self.video_writer = cv2.VideoWriter(self.output_file_name, self.codec, self.fps, self.resolution)
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live", 480, 270)
        self.frame_taking_loop()

    def stop_recording(self):
        self.is_recording = False
        self.recording_button.configure(text= "Start Recording", command=self.start_recording)
        self.timer_seconds = 0
        self.video_writer.release()
        cv2.destroyAllWindows()

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    app.run()
