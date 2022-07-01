from unicodedata import name


class Module:
    def __init__(self, id, name, module, semester):
        self.id = id
        self.name = name
        self.module = module
        self.semester = semester