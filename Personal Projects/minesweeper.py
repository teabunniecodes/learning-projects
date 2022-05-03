import random

class Minesweeper:
    # build board and define how many mines/level
    boardRows = 16
    boardCols = 16
    numMines = 40
    setMines = set()
    mines = 0
    def makeBoard(self):
            # beginner = 9x9 w/ 10 mines
            # intermediate = 16x16 w/ 40 mines
            # advanced = 30x16 w/ 99 mines
        self.board = [["O" for _ in range(self.boardRows)] for _ in range(self.boardCols)]
        for x in self.board: # try to use 2 loops to print without list
            print(" ".join(x))
        
    def placeMines(self):
        # check how many mines we have placed
        # if self.mines <= self.numMines:
            # randomly place the mines / find coordinates for row and colum
            self.setMines.add(((random.choice(range(self.boardRows))), (random.choice(range(self.boardCols)))))
            print(self.setMines)
            # check if a mine is already there
                # if the no mine / replace the space with mine
                    # if true will add a mine to the counter
            self.mines += 1
                # if there is a mine already there, pass
            



                

minesweeper = Minesweeper()
# minesweeper.makeBoard()
minesweeper.placeMines()


# check each space to see if there is a mine next to it (when creating the board)
    # if there is a mine, counter will go up (at most will have 8)
    # assign the numbers in spaces next to the mine

# game play psuedo code starts with board being printed in the terminal
# when coordinate is inputed (row x column) checks the space
    # if mine is there at coordinate - game over
    # if number is there - just uncovers the single space
    # if blank space - uses recursion to keep checking spaces until the space is not blank

# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!