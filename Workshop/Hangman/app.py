from flask import Flask, render_template, request
from Hangman import Hangman

app = Flask(__name__)

# create hangman instance
hangman = Hangman()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        hangman.start_game()
        return render_template('game.html', hangman=hangman)
    if request.method == "POST":
        hangman.guess(request.form['letter'])
        # check if won or lost and render corresponding template
        if hangman.win:
            return render_template('win.html')
        if hangman.lost:
            return render_template('lost.html')
        return render_template('game.html', hangman=hangman)
    
if __name__ == "__main__":
    app.run()