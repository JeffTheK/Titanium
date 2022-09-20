#!/usr/bin/env python3

import os

PIP_REQUIREMENTS = [ "pygubu", "pyautogui", "opencv-python" ]

os.system("pip install " + " ".join(PIP_REQUIREMENTS))