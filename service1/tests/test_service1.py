from flask import url_for
from flask_testing import TestCase
from application import app, db
import requests_mock

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/ticket', json = {'lottery_ticket':[1, 2, 3, 4, 5, 6]})
            m.get('http://service3:5002/lottery', json = {'winning_numbers':[1, 2, 3, 4, 5, 6]})
            m.post('http://service4:5003/prize', json = 10000)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"You bought a lottery ticket with the numbers:", response.data)
            self.assertIn(b"[1, 2, 3, 4, 5, 6]", response.data)

    def test_database(self):
        with requests_mock.Mocker() as m:
            tests = [([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 10000), ([1, 5, 10, 15, 17, 20], [2, 6, 7, 9, 14, 16], 0)]
            for case in tests:
                m.get('http://service2:5001/ticket', json = case[0])
                m.get('http://service3:5002/lottery', json = case[1])
                m.post('http://service4:5003/prize', json = case[2])
                response = self.client.get(url_for('home'))
            self.assertIn(b"Ticket: [1, 2, 3, 4, 5, 6]", response.data)
            self.assertIn(b"Ticket: [1, 5, 10, 15, 17, 20]", response.data)