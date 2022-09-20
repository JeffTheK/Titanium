#!/usr/bin/env python3

import os
import pathlib

path = pathlib.Path(__file__).parent.parent

command = f"cd {path} && python3 -m core_apps.desktop.src.main"

os.system(command)