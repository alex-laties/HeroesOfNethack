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
        print json

        return json
    elif command == "exit":
        sys.exit(0)

        return "OK"
    else:
        return "BAD"