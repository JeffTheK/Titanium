import sys

SUPPORTED_LANGUAGES = ["python"]
OUT_TEXT = ""

def run_code(code, language):
    if language == "python":
        return run_python_code(code)
    else:
        raise Exception

def run_python_code(code):
    global OUT_TEXT
    OUT_TEXT = ""
    original_stdout_write = sys.stdout.write
    original_stderr_write = sys.stderr.write
    sys.stdout.write = stdout_write_redirector
    sys.stderr.write = stdout_write_redirector

    output = None
    try:
        output = exec(code)
    except Exception as e:
        output = e

    sys.stdout.write = original_stdout_write
    sys.stderr.write = original_stderr_write

    return (output, OUT_TEXT)

def stdout_write_redirector(input_str):
    global OUT_TEXT
    OUT_TEXT += input_str