from flask import url_for
from flask_testing import TestCase
from service2.app import app, lottery_ticket
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG = True)
        return app


tests = [({'lottery_ticket':[1, 2, 3, 4, 5, 6]}, {'winning_numbers':[1, 2, 3, 4, 5, 6]}, 10000), 
         ({'lottery_ticket':[1, 2, 3, 4, 5, 6]}, {'winning_numbers':[7, 8, 9, 10, 11, 12]}, 0), 
         ({'lottery_ticket':[1, 2, 3, 4, 5, 6]}, {'winning_numbers':[1, 2, 7, 8, 9, 10]}, 10)]

class TestViews(TestBase):
    def test_get_ticket(self):
        response = self.client.get(url_for("ticket"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data.decode(), lottery_ticket)

        # for case in tests:
        #     with patch("random.choice") as r:
        #         r.return_value = case[0]
        #         response = self.client.get(url_for("ticket"))
        #         self.assertEqual(response.status_code, 200)
        #         self.assertIn(case[0], response.data.decode("utf-8"))