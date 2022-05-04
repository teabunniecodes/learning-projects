import random
import string

class Minesweeper:
    # build board and define how many mines/level
    boardRows = 4
    boardCols = 4
    numMines = 3
    setMines = set()
    flagMines = set()
    countMines = 0
    def makeBoard(self):
            # beginner = 9x9 w/ 10 mines
            # intermediate = 16x16 w/ 40 mines
            # advanced = 30x16 w/ 99 mines
        # starts with board being printed in the terminal
        self.board = [["O" for _ in range(self.boardRows)] for _ in range(self.boardCols)]
        for x in self.board: # try to use 2 loops to print without list
            self.gameBoard = " ".join(x)
            print(self.gameBoard)
        
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

    def placeNums(self):
        self.count = 0
        for coords in self.setMines:
                print(coords)
        # we need to pull coordinates from the set of Mines
            # run through checking the coordinates surrounding the mines and assigning value to the coord
                # use a dictionary with the number space coordinates as the key
                    # value will be the number of mines that it is touching
# check for adjacents in 2d array
        # add count to top left
        # (r - 1, c - 1)

        # add count to top center
        # (r - 1, c)

        # add count to top right
        # (r - 1, c + 1)

        # add count to left side
        # (r, c - 1)

        # add count to right side
        # (r, c + 1)

        # add count to bottom left
        # (r + 1, c - 1)

        # add count to bottom center
        # (r + 1, c)

        # add count to bottom right
        # (r + 1, c + 1)

    def userMove(self):
        # when coordinate is inputed (row x column) checks the space
        self.move = input("Please enter a coordinate: ")
        self.move = self.move.translate(str.maketrans(string.punctuation, (" " * len(string.punctuation))))
        self.move = tuple(map(int, self.move.split()))

    def checkMove(self):
        # if mine is there at coordinate - game over
        if self.move in self.setMines:
            print("Game Over!")
        # if self.move != self.setMines:
            # if blank space - uses recursion to keep checking spaces until the space is not blank

            # if number is there - just uncovers the single space


    # def uncoverSpace(self):


                

minesweeper = Minesweeper()
minesweeper.makeBoard()
minesweeper.placeMines()
minesweeper.userMove()
minesweeper.checkMove()
minesweeper.placeNums()


# check each space to see if there is a mine next to it (when creating the board)
    # if there is a mine, counter will go up (at most will have 8)
    # assign the numbers in spaces next to the mine




# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!