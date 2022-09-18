import os

def run_code(code):
    file = open("tmp.c", "w")
    print(code)
    file.write(code)
    file.close()
    os.system("gcc tmp.c -o tmp.exe")
    output_stream = os.popen("./tmp.exe")
    output = output_stream.read()
    os.remove("tmp.c")
    os.remove("tmp.exe")
    return None, output