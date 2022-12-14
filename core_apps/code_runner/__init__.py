import sys

SUPPORTED_LANGUAGES = ["python", "c", "c++", "bash"]
OUT_TEXT = ""

def run_code(code, language):
    if language == "python":
        from . import python
        return python.run_code(code)
    elif language == "c":
        from . import c
        return c.run_code(code)
    elif language == "c++":
        from . import cpp
        return cpp.run_code(code)
    elif language == "bash":
        from . import bash
        return bash.run_code(code)
    else:
        raise Exception