#!/usr/bin/env python2
import web

urls = (
    "/", "index"
    "/client/(.+)", "client"
)

class index:
    def GET(self):
        f = open("../client/index.html", "r")
        return f.read()

class index:
    def GET(self, name):
        f = open("../client/" + name, "r")
        return f.read()

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
