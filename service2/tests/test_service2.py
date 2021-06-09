from flask import url_for
from flask_testing import TestCase
from service2.app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG = True)
        return app


tests = [([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 10000), 
         ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], 0), 
         ([1, 2, 3, 4, 5, 6], [1, 2, 7, 8, 9, 10], 10)]

class TestViews(TestBase):
    def test_get_ticket(self):

        for case in tests:
            with patch("random.sample") as r:
                r.return_value = case[0]
                response = self.client.get(url_for("ticket"))
                self.assertEqual(response.status_code, 200)
                self.assertIn(case[0], response.data.decode("utf-8"))