import unittest
import web
# from flask import json, jsonify


class WebTestCase(unittest.TestCase):

    def setUp(self) -> None:
        web.app.testing = True
        self.app = web.app.test_client()

    def test_home(self):
        result = self.app.get("/")
        #data = json.loads(result.data)
        string_return = result.data.decode("utf-8")
        self.assertEqual(string_return, "Index Page")