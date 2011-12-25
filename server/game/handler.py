did_world_init = False
worlds = {}

def handle(command, session):
    if (session.world_id not in worlds):
        worlds[session.world_id] = World()

    if command == "server_print":
        print worlds[session.world_id]
    elif command == "exit":
        import sys
        sys.exit(0)
    else
        return "unknown request"
