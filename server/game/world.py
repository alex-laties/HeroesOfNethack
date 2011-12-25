import cell

class World:
    size = 16
    def __init__(self):
        self.cells = []
        for x in xrange(world.size):
            self.cells.append([])
            for y in xrange(world.size):
                self.cells[x].append(cell.Cell())

    def __str__(self):
        board = ""
        for x in xrange(world.size):
            for y in xrange(world.size):
                board += str(self.cells[x][y])
            board += "\n"

        return board

    def test(self):
        pass
