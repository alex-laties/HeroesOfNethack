#!/usr/bin/env python2
import web

urls = (
    "/", "index"
)

class index:
    def GET(self):
        f = open("../client/index.html", "r")
        return f.read()

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
