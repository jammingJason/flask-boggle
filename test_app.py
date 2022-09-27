from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        print('Inside setup')

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>', html)

    # def test_start_game(self):
    #     with app.test_client() as client:
    #         res = client.get('/start-game', 50)
    #         html = res.get_data(as_text=True)
    #         # self.assertEqual(res.status_code, 200)
    #         self.assertRaises(KeyError, 'highscore')
    #         # self.assertIn('<h1>', html)

    def test_check_word(self):
        with app.test_client() as client:
            boggle_game = Boggle()
            get_board = boggle_game.make_board
            session['board'] = get_board
            res = client.get('/check-word?word=building')
            html = res.get_data(as_text=True)
            # self.assertEqual(res.status_code, 200)
            self.assertIn('ok', html)

    # def test_set_highscore(self):
    #     with app.test_client() as client:
    #         print("VJC")
    #         res = client.get('/set-highscore')
    #         html = res.get_data(as_text=True)
    #         # self.assertEqual(res.status_code, 200)
    #         # self.assertIn('<h1>', html)

    # def test_count(self):
    #     with app.test_client() as client:
    #         res = client.post('/count', data={'times_visited': 5})
    #         html = res.get_data(as_text=True)
    #         # self.assertEqual(res.status_code, 200)
    #         # self.assertIn('<h1>', html)
