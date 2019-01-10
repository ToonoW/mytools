import tornado.web

from mytools.publish_request import PublishRequestHandler, TransferRequestHandler


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/tran', TransferRequestHandler),
            (r'/tran/publish-channel', PublishRequestHandler),
        ]
        tornado.web.Application.__init__(self, handlers)
