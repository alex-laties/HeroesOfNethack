#!/usr/bin/env python2
import web

urls = (
    "/", "index"
)

class index:
    def GET(self):
        return "<b><i>Hello, World!</i></b>"

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
