
from crypt import methods
from boggle import Boggle
from flask import Flask, request, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def index():
    """Go to the homepage"""
    if 'highscore' in session:
        highscore = session['highscore']
    else:
        session['highscore'] = 0
    if 'times_visited' in session:
        times_visited = session['times_visited'] + 1
        session['times_visited'] = times_visited
    else:
        session['times_visited'] = 1
    return render_template('index.html')


@app.route('/start-game')
def start_game():
    """Start a new game"""
    new_board = boggle_game.make_board()
    session['board'] = new_board

    return render_template('start-game.html', highscore=session['highscore'], times_visited=session['times_visited'])


@app.route('/check-word')
def check_word():
    """Check to see if the word is valid and on the board"""
    str_word = request.args['word']
    check_status = boggle_game.check_valid_word(session['board'], str_word)
    return check_status


@app.route('/set-highscore')
def set_highscore():
    if request.args:
        if int(session['highscore']) <= int(request.args['score']):
            session['highscore'] = request.args['score']
    return session['highscore']
