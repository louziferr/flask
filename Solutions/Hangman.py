from random import choice

class Hangman:
    '''class for hangman game'''
    def __init__(self):
        self.wordlist = ["workshop", "python", "berlin", "feminism", "programming", "language"]
        self.start_game()

    def start_game(self):
        # setting everything up for a new game
        self.win = False
        self.lost = False
        self.word = choice(self.wordlist)
        self.current_word = ["_" for x in self.word]
        self.guessed = list()
        self.lives = 8
    
    def guess_letter(self, letter):
        # processing a guess
        if len(letter) != 1:
            # wrong kind of input (ignoring for now)
            return
        letter = letter.lower()
        if letter in self.word:
            # correct guess: replace characters in string
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.current_word[i] = letter
            if "_" not in self.current_word:
                # winning
                self.win = True

        elif letter not in self.guessed:
            # wrong guess
            self.lives -= 1
            self.guessed.append(letter)
            if self.lives < 0:
                # loosing
                self.lost = True