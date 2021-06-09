from flask import url_for
from flask_testing import TestCase
from service4.app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG = True)
        return app

tests = [([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 10000), 
         ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], 0), 
         ([1, 2, 3, 4, 5, 6], [1, 2, 7, 8, 9, 10], 5)]

class TestViews(TestBase):
    def test_get_prize(self):
        for case in tests:
            send = {'ticket':case[0], 'lottery':case[1]}
            response = self.client.post(url_for("prize"), json = send)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(case[2], response.json)