# this is for computer to select a random word from a text file

# create a class for hangman
# limit the amount of wrong guesses to 6
    # each time a wrong guess remove 1 from tries left
# computer pulls random word from file
    # find the length of the word but don't show it
    # turns the word into a list
    # prints the subject of the word on screen as a hint
# display "_ " for each letter space
    # turns it into a list so correct letters are replaced in the array
    # prints out the new list with blanks and letters each time there is a correct guess
# user starts to guess the letters
    # asks user for input - checks if it is one letter
        # checks against the letters in the original list
    # user can guess the word by pressing number 1
        # computer will compare the string to original string if it matches
            # matches user wins
            # doesn't match, computer wins! (doesn't matter how many tries left)