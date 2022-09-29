import os
import json

def run_project(path, args=None):
    project_file = open(os.path.join(path, ".project.json"), "r")
    project_json = json.loads(project_file.read())
    run_command = project_json["run_command"]
    if args != None:
        run_command += " " + args
    run_command += " &"
    os.system(run_command)