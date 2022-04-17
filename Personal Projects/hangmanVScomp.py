# this is for computer to select a random word from a text file
import random

# create a class for hangman
class hangMan:
    def __init__(self):
        self.turns = 6
        # set the list of letters
        self.guessed = set()

    def theWord(self):
        # computer pulls random word from file
        with open("Personal Projects\Text Files\wordlist.txt") as read:
            words = list(map(str, read))
            self.chosenWord = random.choice(words).strip()
            self.chosenWord = self.chosenWord.upper()
            print(self.chosenWord)
            # find the length of the word but don't show it
            self.guessWord = ["-"] * len(self.chosenWord)
            # display "_ " for each letter space
                # turns it into a list so correct letters are replaced in the array
            print(f"Guess the word: {''.join(self.guessWord)}")

    # limit the amount of wrong guesses to 6
    def turnsLeft(self):
        # each time a wrong guess remove 1 from tries left
        self.turns -= 1
        print(f"You have {self.turns} turn(s) left")

    def guesses(self):
        while self.turns > 0:
            # asks user for input and turns input into upper case
            self.guess = input("Please input a letter or guess: ").upper()
            self.checkGuess()

    def checkGuess(self):
        # checks if it is one letter
        if len(self.guess) == 1 and self.guess.isalpha():
            # check if the letter has been guessed yet
            if self.guess in self.guessed:
                print("You have already guessed this letter.")
                print(f"Letters you have chosen: {set(self.guessed)}")
                self.guesses()
            elif self.guess != self.guessed:
                if self.guess in self.chosenWord:
                    self.guessed.add(self.guess)
                    x = self.chosenWord.find(self.guess)
                    self.guessWord[x] = self.guess
                # prints out the letters in the correct spaces
                print(''.join(self.guessWord))
                if self.guess not in self.chosenWord:
                    self.guessed.add(self.guess)
                    print(f"Sorry, letter {self.guess} is not in the word")
                    self.turnsLeft()
        self.invalidGuess()
        self.userWin()
        self.userLose()

    def invalidGuess(self):
        # when user inputs more than 1 letter and less than word length give error
        if (len(self.guess) > 1 and len(self.guess) < len(self.chosenWord)) or len(self.guess) > len(self.chosenWord):
            print("Please input a one letter or a valid guess")
            self.guesses()

    def userWin(self):
        # computer will compare the string to original string if it matches
        # matches user wins
        if self.guess == self.chosenWord: #when user correctly guesses
            self.turns = 0
            print("You Win!")

    def userLose(self):
        # doesn't match, computer wins! (doesn't matter how many tries left)
        if self.guess != self.chosenWord and len(self.guess) == len(self.chosenWord):
            self.turns = 0
            if self.turns == 0:
                print("Game Over!")

# figure out how to check for duplicates in the word

hangman = hangMan()
hangman.theWord()
hangman.guesses()