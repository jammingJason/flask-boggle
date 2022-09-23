
from boggle import Boggle
from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start-game')
def start_game():
    new_board = boggle_game.make_board()
    session['board'] = new_board
    return render_template('start-game.html', new_board=new_board)


@app.route('/check-word')
def check_word():
    str_word = request.args['word']
    check_status = boggle_game.check_valid_word(session['board'], str_word)
    return render_template('start-game.html', check_status=check_status)
