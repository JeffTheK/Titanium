#!/usr/bin/env python3

import os
import pathlib

this_file_path = pathlib.Path(__file__).parent.absolute()
tkfontawesome_path = this_file_path.joinpath('tkfontawesome/.')
launch_py_path = this_file_path.joinpath("launch.py")

os.system(f"pip install {tkfontawesome_path}")
os.system(f"python3 {launch_py_path}")