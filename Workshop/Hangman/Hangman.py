from random import choice

class Hangman:
    def __init__(self):
        self.wordlist = ["python", "workshop", "hangman", "berlin"]
        self.start_game()

    def start_game(self):
        self.win = False
        self.lost = False
        self.word = choice(self.wordlist)
        self.current_word = ["_" for l in self.word]
        self.guessed = []
        self.lives = 8

    def guess(self, letter):
        if len(letter) != 1:
            # letter is longer than 1 symbol
            return
        letter = letter.lower()
        if letter in self.word:
            # correct guess
            for i in range(len(self.word)):
                # find position of letter
                if self.word[i] == letter:
                    self.current_word[i] = letter
            # check if user has won
            self.win = "_" not in self.current_word    
        elif letter not in self.guessed:
            # wrong guess
            self.lives -= 1
            self.guessed.append(letter)
            # check if user has lost
            self.lost = self.lives < 0
