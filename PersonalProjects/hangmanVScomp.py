# this is for computer to select a random word from a text file
import random

# create a class for hangman
class hangMan:
    def __init__(self):
        self.chosen_word=self.generateRandomWord()
        self.turns = len(self.chosen_word)+1
        # set the list of letters
        self.guessed = list()
        self.correct_guess=list()
        self.guesses()

    """ Generates Random Word
        no input
        return str
    """
    def generateRandomWord(self) -> str:
            # computer pulls random word from file
            read = open("TextFiles/wordlist.txt","r")
            words = list(map(str, read))
            chosenWord = random.choice(words).strip()
            chosenWord = chosenWord.upper()
            print(chosenWord)
            # find the length of the word but don't show it
            self.guessWord = ["-"] * len(chosenWord)
            # display "_ " for each letter space
            # turns it into a list so correct letters are replaced in the array
            print(f"Guess the word: {''.join(self.guessWord)}")
            return chosenWord


    """ guesses - starts game
        input
        return nothing
    """
    def guesses(self) -> None:
        while self.turns > 0:
            # asks user for input and turns input into upper case
            guess = input("Please input a letter or guess: ").upper()
            self.checkGuess(guess, self.chosen_word)

    """check Guess
        input guess, chosen_word
        return none
    """
    def checkGuess(self,guess,chosen_word)-> None:
        # checks if input is valid
        isInvalid = self.invalidGuess(guess)
        guessed_before = self.checkIfGuessedBefore(guess)

        # Checks if word contains guess and both isInvalid and guessed_before are true to continue
        if not isInvalid and not guessed_before and chosen_word.__contains__(guess):
            indexes = [index for index, letter in enumerate(chosen_word) if letter == guess]

            # Loop Over Indexes
            for i in indexes:
                self.guessWord[i] = guess
                self.correct_guess.append(guess)

            # prints out the letters in the correct spaces
            print(''.join(self.guessWord))
            self.guessesLeft()
            self.isGameOver()

        # If invalid or guessed before break
        elif isInvalid or guessed_before:
            pass
        else:
            print(f"Sorry, letter {guess} is not in the word")
            self.guessed.append(guess)
            self.guessesLeft()
            self.isGameOver()
    """ checkIfGuessedBefore
        input guess
        return bool
    """
    def checkIfGuessedBefore(self,guess) -> bool:
        # check if the letter has been guessed yet
        if guess in self.guessed:
            print("You have already guessed this letter.")
            print(f"Letters you have chosen: {self.guessed}")
            return True
        return False

    """ limit the amount of wrong guesses
        input turns 
        returns None
    """
    def guessesLeft(self) -> None:
        # each time a wrong guess remove 1 from tries left
        self.turns -= 1
        print(f"You have {self.turns} turn(s) left")

    """ Invalid guess 
        input guess
        return bool
    """
    def invalidGuess(self, guess) -> bool:
        # when user inputs more than 1 letter and less than word length give error
        if len(guess) > 1 or not guess.isalpha():
            print("Please input a one letter only!")
            return True
        return False

    """ Checks if Game is over
        return none
    """
    def isGameOver(self) -> None:
        # computer will compare the string to original string if it matches
        correct_word=''
        word_len=len(self.chosen_word)
        answer_len=0
        finished = False

        for letter in self.correct_guess:
            if letter in self.chosen_word:
                answer_len += 1

        if answer_len==word_len:
            finished = True

        if finished:
            print("You Won!")
            self.playAgain()
        elif self.turns == 0:
            print("sorry you lose!")
            self.turns = 0
            self.playAgain()
            
    """PlayAgain checks if users wants to play again
        input none
        return none
    """
    def playAgain(self)-> None:
        ans=input("Do you want to play again? (Y/N)? ")
        if  ans.upper()=='Y':
            print("Ok here you go again with a new word")
            hangMan()
        else:
            print("No Problem comeback and play again!")
            exit()

# figure out how to check for duplicates in the word

hangMan()



