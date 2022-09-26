class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.has_unsaved_changes = False