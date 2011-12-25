#!/usr/bin/env python2
import web
web.config.debug = False

urls = (
    "/", "index",
    "(/css/.+)", "staticfiles",
    "(/js/.+)", "staticfiles",
    "/ajax/?(.+)", "ajax",
    "/count", "count",
    "/reset", "reset"
)

app = web.application(urls, globals())
default_session_vars = {}
default_session_vars["count"] = 0
session = web.session.Session(app, web.session.DiskStore("sessions"),
                              initializer = default_session_vars)

class index:
    def GET(self):
        f = open("../client/index.html", "r")
        return f.read()

class staticfiles:
    def GET(self, name):
        f = open("../client/{0}".format(name), "r")
        return f.read()

class ajax:
    def GET(self, command):
        import game.handler
        return game.handler.handle(command, session)

class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return "reset!"

if __name__ == "__main__":
    app.run()
