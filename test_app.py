from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>', html)

    def test_start_game(self):
        with app.test_client() as client:
            res = client.get('/start-game')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>', html)

    def test_check_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                # Modify the session in this context block.
                sess["board"] = Boggle.make_board(self)
            res = client.get('/check-word?word=make')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('not-on-board', html)

    def test_set_highscore(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                # Modify the session in this context block.
                sess["highscore"] = "0"
            res = client.get('/set-highscore?score=100')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('100', html)
