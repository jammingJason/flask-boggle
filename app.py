
from boggle import Boggle
from flask import Flask, request, render_template, session, redirect, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
# debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def index():
    """Go to the homepage"""
    return render_template('index.html')


@app.route('/start-game')
def start_game():
    """Start a new game"""
    get_board()
    get_highscore()
    getCount()
    return render_template('start-game.html')


@app.route('/get-board')
def get_board():
    new_board = boggle_game.make_board()
    session['board'] = new_board
    return new_board


@app.route('/check-word')
def check_word():
    """Check to see if the word is valid and on the board"""
    str_word = request.args['word']
    check_status = boggle_game.check_valid_word(session['board'], str_word)
    return check_status


@app.route('/set-highscore')
def set_highscore():
    """Sets the highscore to a session variable"""
    if request.args:
        if int(session['highscore']) <= int(request.args['score']):
            session['highscore'] = request.args['score']
    return session['highscore']


@app.route('/get-highscore')
def get_highscore():
    """Gets the highscore"""
    if 'highscore' in session:
        highscore = session['highscore']
    else:
        session['highscore'] = 0
        highscore = session['highscore']
    return highscore


@app.route('/count', methods=['POST'])
def count():
    return 'VJC'


@app.route('/get-count')
def getCount():
    if 'times_visited' in session:
        session['times_visited'] = int(session['times_visited']) + 1
    else:
        session['times_visited'] = 1
    return session['times_visited']
