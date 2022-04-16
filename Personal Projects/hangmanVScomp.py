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
        print("You have {turns} turn(s) left")

    def guesses(self):
        while self.turns > 0:
            # asks user for input and turns input into upper case
            guess = input("Please input a letter or guess: ").upper()
            print(guess)
            # checks if it is one letter
            if len(guess) == 1 and guess.isalpha():
                # check if the letter has been guessed yet
                if guess in self.guessed:
                    print("You have already guessed this letter.")
                    print(f"Letters you have chosen: {self.guessed}")
                elif guess == self.chosenWord: #when user correctly guesses
                    self.guessed.add(guess)
                    if guess in self.chosenWord:
                        x = self.chosenWord.find(guess)
                        self.guessWord[x] = guess
                        # prints out the letters in the correct spaces
                        print(''.join(self.guessWord))
                elif guess != self.chosenWord: # when user incorrectly guesses
                    turns = 0
                    print("Game Over!")

# figure out how to check for duplicates in the word
# when user inputs more than 1 letter and less than word length give error
# figure out how/when to count down turns during wrong guesses

        # computer will compare the string to original string if it matches
            # matches user wins
            # doesn't match, computer wins! (doesn't matter how many tries left)

hangman = hangMan()
hangman.theWord()
hangman.guesses()