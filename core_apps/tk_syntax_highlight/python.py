import tkinter as tk

KEY_WORDS = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'try', 'while', 'with', 'yield'
]

DELIMITERS = ["\n", " ", ":"]

def highlight(code, text_widget: tk.Text):
    out = code
    text_widget.tag_configure("key_word", foreground="red")
    text_widget.tag_configure("string", foreground="green")
    text_widget.tag_configure("number", foreground="blue")
    text_widget.tag_configure("function_call", foreground="#38c4d9")
    text_widget.tag_configure("function_declaration", foreground="#1de085")
    text_widget.tag_configure("const_variable", foreground="magenta")
    pos_l = 1
    pos_c = 0
    i = 0
    current_word = ""
    previous_word = ""
    while i != len(out):
        char = out[i]

        #print(f"{pos_l}.{pos_c}")

        if char in DELIMITERS:
            if current_word in KEY_WORDS:
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                #print(f"{pos_l}.{pos_c - len(current_word)}")
                #print(f"{pos_l}.{pos_c}")
                text_widget.tag_add("key_word", "matchStart", "matchEnd")
            elif current_word == "=":
                pass
            elif current_word.replace(".", "").isnumeric():
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                text_widget.tag_add("number", "matchStart", "matchEnd")
            elif len(current_word) >= 2 and current_word[0] == '"' and current_word[-1] == '"':
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                text_widget.tag_add("string", "matchStart", "matchEnd")
            elif len(current_word) >= 3 and current_word[-1] == ")" and previous_word != "def":
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                text_widget.tag_add("function_call", "matchStart", "matchEnd")
            elif len(current_word) >= 3 and current_word[-1] == ")" and previous_word == "def":
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                text_widget.tag_add("function_declaration", "matchStart", "matchEnd")
            elif current_word == current_word.upper():
                text_widget.mark_set("matchEnd", f"{pos_l}.{pos_c}")
                text_widget.mark_set("matchStart", f"{pos_l}.{pos_c - len(current_word)}")
                text_widget.tag_add("const_variable", "matchStart", "matchEnd")
            previous_word = current_word
            current_word = ""
        else:
            current_word += char

        if char == "\n":
            pos_l += 1
            pos_c = 0
        else:
            pos_c += 1
        i += 1

    return out