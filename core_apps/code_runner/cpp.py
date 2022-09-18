import os

def run_code(code):
    file = open("tmp.cpp", "w")
    file.write(code)
    file.close()
    os.system("g++ tmp.cpp -o tmp.exe")
    output_stream = os.popen("./tmp.exe")
    output = output_stream.read()
    os.remove("tmp.cpp")
    os.remove("tmp.exe")
    return None, output