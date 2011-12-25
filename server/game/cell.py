class Cell:
    def __init__(self):
        # will be ground by default
        self.char = '.'
        # white color by default
        self.color = "FFFFFF"
        # objects in this cell
        self.objects = []

    def __str__(self):
        if len(self.objects) > 0:
            return self.objects[-1].char
        else:
            return self.char

    def jsonify(self):
        if len(self.objects) > 0:
            return self.objects[-1].jsonify()
        else:
            dict = {}

            dict['c'] = "#" + self.color
            dict['r'] = self.char

            return dict
