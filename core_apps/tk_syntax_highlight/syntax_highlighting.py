def highlight(code, language, text_widget):
    if language == "python":
        from . import python
        return python.highlight(code, text_widget)
