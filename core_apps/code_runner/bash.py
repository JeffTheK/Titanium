import os

def run_code(code):
    file = open("tmp.bash", "w")
    file.write(code)
    file.close()
    output_stream = os.popen("bash tmp.bash")
    output = output_stream.read()
    os.remove("tmp.bash")
    return None, output