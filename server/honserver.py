#!/usr/bin/env python2
import web

urls = (
    "/", "index",
    "(/css/.+)", "static",
    "(/js/.+)", "static",
    "/ajax?(.+)", "ajax"
)

class index:
    def GET(self):
        f = open("../client/index.html", "r")
        return f.read()

class static:
    def GET(self, name):
        f = open("../client/{0}".format(name), "r")
        return f.read()

class ajax:
    def GET(self, command):
        print command
        return "not yet"

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
