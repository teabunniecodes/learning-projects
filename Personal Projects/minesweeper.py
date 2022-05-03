import random
import string

class Minesweeper:
    # build board and define how many mines/level
    boardRows = 16
    boardCols = 16
    numMines = 40
    setMines = set()
    countMines = 0
    def makeBoard(self):
            # beginner = 9x9 w/ 10 mines
            # intermediate = 16x16 w/ 40 mines
            # advanced = 30x16 w/ 99 mines
        # starts with board being printed in the terminal
        self.board = [["O" for _ in range(self.boardRows)] for _ in range(self.boardCols)]
        for x in self.board: # try to use 2 loops to print without list
            print(" ".join(x))
        
    def placeMines(self):
        # check how many mines we have placed
        while self.countMines < self.numMines:
            # randomly place the mines / find coordinates for row and colum
            coorMine = random.choice(range(self.boardRows)), random.choice(range(self.boardCols))
            # check if a mine is already there
            # if there is a mine already there, pass
            if coorMine in self.setMines:
                pass
            # if the no mine / replace the space with mine
            elif coorMine != self.setMines:
                self.setMines.add(coorMine)
                # if true will add a mine to the counter
                self.countMines += 1
        print(self.setMines)

    def userMove(self):
        # when coordinate is inputed (row x column) checks the space
        move = input("Please enter a coordinate: ")
        move = move.translate(str.maketrans(string.punctuation, (" " * len(string.punctuation))))
        move = move.split()
        move = tuple(map(int, move))
            # if mine is there at coordinate - game over
            # if number is there - just uncovers the single space
            # if blank space - uses recursion to keep checking spaces until the space is not blank




                

minesweeper = Minesweeper()
# minesweeper.makeBoard()
minesweeper.placeMines()
minesweeper.userMove()


# check each space to see if there is a mine next to it (when creating the board)
    # if there is a mine, counter will go up (at most will have 8)
    # assign the numbers in spaces next to the mine




# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!