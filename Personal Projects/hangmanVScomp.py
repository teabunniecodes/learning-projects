# this is for computer to select a random word from a text file
import random

# create a class for hangman
class hangMan:
    def __init__(self):
        self.turns = 6
        # set the list of letters
        self.guessed = set()

    def getWord(self):
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
    def showTurns(self):
        # each time a wrong guess remove 1 from tries left
        print(f"You have {self.turns} turn(s) left")

    def getGuess(self):
        while self.turns > 0:
            # asks user for input and turns input into upper case
            self.guess = input("Please input a letter or guess: ").upper()
            # ty liplounge!  add [0] to end of input (restricts input to one character)
            self.checkGuess()
            self.isInvalid()
            self.getLose()
            self.isWin()
            self.isLose()

    def checkGuess(self):
        # checks if it is one letter
        if len(self.guess) == 1 and self.guess.isalpha():
            # check if the letter has been guessed yet
            if self.guess in self.guessed:
                print("You have already guessed this letter.")
                print(f"Letters you have chosen: {set(self.guessed)}")
            elif self.guess != self.guessed:
                # loops through to check duplicate letters and assign to the index
                for index, letter in enumerate(self.chosenWord):
                    self.guessed.add(self.guess)
                    if self.guess == self.chosenWord[index] and self.guess == letter:
                        self.guessWord[index] = self.guess
                # prints out the letters in the correct spaces
                print(''.join(self.guessWord))
                if self.guess not in self.chosenWord:
                    self.guessed.add(self.guess)
                    print(f"Sorry, letter {self.guess} is not in the word")
                    self.turns -= 1
                    self.showTurns()

    def isInvalid(self):
        # when user inputs more than 1 letter and less than word length give error
        if (len(self.guess) > 1 and len(self.guess) < len(self.chosenWord)) or len(self.guess) > len(self.chosenWord):
            print("Please input a one letter or a valid guess")

    def getLose(self):
        # doesn't match, computer wins! (doesn't matter how many tries left)
        if self.guess != self.chosenWord and len(self.guess) == len(self.chosenWord):
            self.turns = 0

    def isWin(self):
        # computer will compare the string to original string if it matches
        # matches user wins
        if self.guess == self.chosenWord: #when user correctly guesses
            print("You Win!")

    def isLose(self):
        # if there are no more turns left and the user hasn't won
        if self.turns == 0:
            print("Game Over!")

# figure out how to check for duplicates in the word

hangman = hangMan()
hangman.getWord()
hangman.getGuess()