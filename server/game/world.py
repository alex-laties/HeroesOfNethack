import cell
import json
import player
import random

class World:
    # hardcoded constants
    size = 16

    def __init__(self):
        # init all the cells of the world
        self.cells = []
        for x in xrange(World.size):
            self.cells.append([])
            for y in xrange(World.size):
                self.cells[x].append(cell.Cell())

        # this dict will store all the players
        self.players = {}

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

    def ready_player(self, session):
        print session.session_id
        if session.session_id not in self.players:
            new_player = player.Player()
            self.players[session.session_id] = new_player
            while True:
                x = random.randint(0, World.size - 1)
                y = random.randint(0, World.size - 1)

                flag = False

                for obj in self.cells[x][y].objects:
                    if isinstance(obj, player.Player):
                        flag = True

                if flag == True:
                    continue

                self.cells[x][y].objects.append(new_player)
                new_player.container = self.cells[x][y]

                break
        else:
            # we are already ready
            pass

    def move_player(self, session, x_offset, y_offset):
        p = self.players[session.session_id]
        cur_x = p.container.x
        cur_y = p.container.y

        new_x = cur_x + x_offset
        new_x = max(0, min(new_x, World.size - 1))
        new_y = cur_y + y_offset
        new_y = max(0, min(new_y, World.size - 1))

        if ((new_x != cur_x) or (new_y != cur_y)):
            old_cell = self.cells[cur_x][cur_y]
            old_cell.objects.remove(p)
            new_cell = self.cells[new_x][new_y]
            new_cell.objects.append(p)
            player.container = new_cell
