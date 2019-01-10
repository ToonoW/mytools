import tornado.httpserver
import tornado.ioloop
from mytools.app import Application


if __name__ == "__main__":
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
