import cell
import json

class World:
    # hardcoded constants
    size = 16

    def __init__(self):
        self.cells = []
        for x in xrange(World.size):
            self.cells.append([])
            for y in xrange(World.size):
                self.cells[x].append(cell.Cell())

    def __str__(self):
        board = ""
        for x in xrange(World.size):
            for y in xrange(World.size):
                board += str(self.cells[x][y])
            board += "\n"

        return board

    def jsonify(self):
        snapshot = []
        for x in xrange(World.size):
            snapshot.append([])
            for y in xrange(World.size):
                cell_snapshot = self.cells[x][y].jsonify()
                cell_snapshot['x'] = str(x)
                cell_snapshot['y'] = str(y)
                snapshot[x].append(cell_snapshot)

        return json.dumps(snapshot, separators=(',', ':'))

    def test(self):
        pass
