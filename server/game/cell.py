class Cell:
    def __init__(self):
        # will be ground by default
        self.char = '.'
        # white color by default
        self.color = "FFFFFF"
        # objects in this cell
        self.objects = []

    def __str__(self):
        return self.char
