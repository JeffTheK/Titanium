def cli(args, transcript):
    for i, arg in enumerate(args):
        if arg == "-text":
            transcript.edit_area.text.insert("1.0", args[i + 1])