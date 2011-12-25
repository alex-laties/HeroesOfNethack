import sys
from world import World

did_world_init = False
worlds = {}

def handle(command, session):
    # make sure world exists, otherwise create it
    if (session.world_id not in worlds):
        worlds[session.world_id] = World()

    if command == "server_print":
        print worlds[session.world_id]

        return "OK"
    elif command == "snapshot":
        json = worlds[session.world_id].jsonify()

        return json
    elif command == "ready_player":
        worlds[session.world_id].ready_player(session)

        return "OK"
    elif command == "exit":
        sys.exit(0)

        return "OK"

    elif command == "left":
        worlds[session.world_id].move_player(session, -1, 0)
    elif command == "right":
        worlds[session.world_id].move_player(session, 1, 0)
        pass
    elif command == "top":
        worlds[session.world_id].move_player(session, 0, -1)
        pass
    elif command == "bottom":
        worlds[session.world_id].move_player(session, 0, 1)
        pass
    else:
        return "BAD"
