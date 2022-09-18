import os

PROJECT_JSON_FILE_TEMPLATE = """ {
    "run_command": "python3 -m core_apps.PROJECT_NAME.src.main"
}
"""

def create_python_project(project_name, project_path):
    os.mkdir(project_path)
    os.mkdir(project_path / "src")
    create_project_json_file(project_name, project_path)

def create_project_json_file(project_name, project_path):
    project_json_file = open(os.path.join(project_path, ".project.json"), "w")
    project_json_file.write(PROJECT_JSON_FILE_TEMPLATE.replace("PROJECT_NAME", project_name))
    project_json_file.close()