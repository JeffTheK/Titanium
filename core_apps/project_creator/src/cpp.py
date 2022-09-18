import os

PROJECT_JSON_FILE_TEMPLATE = """ {
    "run_command": "make run"
}
"""

MAKEFILE_TEMPLATE = """COMPILER = g++

build:
\t$(COMPILER) src/*.cpp -o PROJECT_NAME.exe

run: build
\t./PROJECT_NAME.exe
"""

MAIN_C_TEMPLATE = """#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "Hello World";
    return 0;
}
"""

def create_cpp_project(project_name, project_path):
    os.mkdir(project_path)
    os.mkdir(project_path / "src")
    create_project_json_file(project_name, project_path)
    create_makefile(project_name, project_path)
    create_main_cpp(project_name, project_path)

def create_makefile(project_name, project_path):
    makefile = open(os.path.join(project_path, "Makefile"), "w")
    makefile.write(MAKEFILE_TEMPLATE.replace("PROJECT_NAME", project_name))
    makefile.close()

def create_main_cpp(project_name, project_path):
    file = open(os.path.join(os.path.join(project_path, "src"), "main.cpp"), "w")
    file.write(MAIN_C_TEMPLATE.replace("PROJECT_NAME", project_name))
    file.close()

def create_project_json_file(project_name, project_path):
    project_json_file = open(os.path.join(project_path, ".project.json"), "w")
    project_json_file.write(PROJECT_JSON_FILE_TEMPLATE.replace("PROJECT_NAME", project_name))
    project_json_file.close()