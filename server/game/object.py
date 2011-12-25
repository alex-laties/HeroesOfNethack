class Object:
    def __init__(self):
        self.char = "?"
        self.color = "FF0000"
        self.container = None

    def jsonify(self):
        dict = {}

        dict['c'] = "#" + self.color
        dict['r'] = self.char

        return dict
