from flask import Flask, render_template, request
from Hangman import Hangman

# the flask app
app = Flask(__name__)

# the hangman object
hangman = Hangman()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=["GET", "POST"])
def game():
    if request.method == "GET":
        hangman.start_game()
        return render_template('game.html', hangman=hangman)
    
    if request.method == "POST":
        hangman.guess_letter(request.form['letter'])
        if hangman.win:
            return render_template('win.html', current_word=hangman.current_word)
        if hangman.lost:
            return render_template('lost.html')
        return render_template('game.html', hangman=hangman)

if __name__ == "__main__":
    app.run()