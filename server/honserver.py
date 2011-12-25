#!/usr/bin/env python2
import web

urls = (
    "/", "index",
    "(/css/.+)", "static",
    "(/js/.+)", "static"
)

class index:
    def GET(self):
        f = open("../client/index.html", "r")
        return f.read()

class static:
    def GET(self, name):
        f = open("../client/{0}".format(name), "r")
        return f.read()

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
