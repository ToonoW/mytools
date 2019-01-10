import json
import logging

import tornado.web
import tornado.websocket


class TransferRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.handle_request()

    def post(self):
        self.handle_request()

    def handle_request(self):
        PublishRequestHandler.publish_request(request=self.request)
        self.write('ok')


class PublishRequestHandler(tornado.websocket.WebSocketHandler):
    waiters = set()

    def check_origin(self, origin):
        return True

    def open(self):
        PublishRequestHandler.waiters.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message("You said: " + message)

    def on_close(self):
        PublishRequestHandler.waiters.remove(self)
        print("WebSocket closed")

    @classmethod
    def publish_request(cls, request):
        detial = """
** URI **
{}

** METHOD **
{}

** HEADER **
{}

** BODY **
{}
        """.format(request.uri, request.method, json.dumps(request.headers._dict, sort_keys=True, indent=2), request.body)
        for waiter in cls.waiters:
            try:
                waiter.write_message(detial)
            except:
                logging.error("Error sending message", exc_info=True)
