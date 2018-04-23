from threading import Thread
from unittest import TestCase
from wsgiref.simple_server import make_server

from core.wsgi import application


class TestServer(TestCase):
    def test_that_server_turns_on_ok_through_wsgi(self):
        httpd = make_server('', 8912, application)
        Thread(target=httpd.serve_forever).start()  # Start in a thread because it blocks the execution
        httpd.shutdown()
