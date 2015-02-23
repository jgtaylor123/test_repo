import unittest

from .hello_app import app


class HelloTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        assert 'Hello' in self.app.get('/').data

    def test_world(self):
        assert 'world' in self.app.get('/').data

    def test_howdy(self):
        assert 'Howdy' in self.app.get('/').data
