import random
import string

class Minesweeper:
    # build board and define how many mines/level
    boardRows = 4
    boardCols = 4
    numMines = 3
    # flagMines = set()
    dictSpace = {}
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
        
        # for r in range(self.boardRows):
        #     for c in range(self.boardCols):
        #         self.dictSpace[(r, c)] = " "
        # print(self.dictSpace)

    def placeMines(self):
        # check how many mines we have placed
        while self.countMines < self.numMines:
            # randomly place the mines / find coordinates for row and colum
            mineRow = random.choice(range(self.boardRows))
            mineCols = random.choice(range(self.boardCols))
            coorMine = mineRow, mineCols
            # check if a mine is already there
            # if there is a mine already there, pass
            if coorMine in self.dictSpace:
                pass
            # if the no mine / replace the space with mine
            elif coorMine != self.dictSpace:
                self.dictSpace[coorMine] = "*"
                # if true will add a mine to the counter
                self.countMines += 1
                self.placeNums(mineRow, mineCols)
        print(self.dictSpace)

    # method will use the coordinates of the mines that are placed
    def placeNums(self, row, col):
        # finds coordinate of top left, top center, top right, left side, right side, bottom left, bottom center, bottom right surrounding the mine
        spaceList = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        # goes through the coordinates one by one
        for space in spaceList:
            # checks to see if the coordinate is a valid coordinate on the board - skips it if it is not
            if space[0] < 0 or space[1] < 0 or space[0] > (self.boardRows - 1) or space[1] > (self.boardCols - 1):
                continue
            # if the coordinate is not in the dictionary yet, adds key and value
            if space not in self.dictSpace:
                self.dictSpace[space] = 1
            # if the coordinate is already a key, increments the value up by 1
            elif space in self.dictSpace and self.dictSpace[space] != "*" and self.dictSpace[space] != "M":
                self.dictSpace[space] += 1

    def userMove(self):
        # when coordinate is inputed (row x column) checks the space
        self.move = input("Please enter a coordinate: ")
        self.move = self.move.translate(str.maketrans(string.punctuation, (" " * len(string.punctuation))))
        self.move = tuple(map(int, self.move.split()))

    def checkMove(self):
        # if mine is there at coordinate - game over
        if self.move in self.dictSpace:
            # uncover space ************
            if self.dictSpace[self.move] != "*":
                print("REPLACE BOARD COORD WITH VALUE")
            else:
                print("Game Over!")
        # if self.move != self.dictSpace:
            # if blank space - uses recursion to keep checking spaces until the space is not blank


    # def uncoverSpace(self):


                

minesweeper = Minesweeper()
minesweeper.makeBoard()
minesweeper.placeMines()
# minesweeper.userMove()
# minesweeper.checkMove()


# check each space to see if there is a mine next to it (when creating the board)
    # if there is a mine, counter will go up (at most will have 8)
    # assign the numbers in spaces next to the mine




# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!