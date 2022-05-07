import random
import string

# echo -e "\e[1;33;40m Yellow on black \e[m"

class Minesweeper:
    # build board and define how many mines/level
    
    # flagMines = set()
    dictBoard = {}
    dictSpace = {}
    countMines = 0
    countFlags = 0
    boardRows = 0
    boardCols = 0
    numMines = 0

    def chooseLevel(self):
        while True:
            level = ["beginner", "intermediate", "advanced", "custom"]
            choice = input("Please choose a level (Beginner, Intermediate, Advanced, Custom): ").lower()
            if choice in level:
                # beginner = 9x9 w/ 10 mines
                if choice == level[0]:
                    self.boardRows = 9
                    self.boardCols = 9
                    self.numMines = 10
                    break
                # intermediate = 16x16 w/ 40 mines
                elif choice == level[1]:
                    self.boardRows = 16
                    self.boardCols = 16
                    self.numMines = 40
                    break
                # advanced = 30x16 w/ 99 mines
                elif choice == level[2]:
                    self.boardRows = 16
                    self.boardCols = 30
                    self.numMines = 99
                    break
                # custom = user inputs their custom level
                elif choice == level[3]:
                    while True:
                        try:
                            ### This causes the program to go on forever placing bombs :(
                            self.boardRows = int(input("Please enter a number 1-80 for rows: "))
                            self.boardCols = int(input("Please enter a number 1-80 for columns: "))
                            self.numMines = int(input("Please enter a number 1-99 for bombs: "))
                            if 0 < self.boardRows <= 80 and 0 < self.boardCols <= 80 and 0 < self.numMines <= 99 and self.numMines < (self.boardRows * self.boardCols) / 2:
                                break
                            # self.boardRows = int(input("Please enter a number 1-20 for rows: "))
                            # self.boardCols = int(input("Please enter a number 1-20 for columns: "))
                            # self.numMines = int(input("Please enter a number 1-60 for bombs: "))
                            # if 0 < self.boardRows <= 20 and 0 < self.boardCols <= 20 and 0 < self.numMines <= 60 and self.numMines < (self.boardRows * self.boardCols) / 2:
                            #     break
                            else: 
                                print("Can't make a board like that! D:")
                        except:
                            print("Can't make a board like that! D:")
                    break
            else:
                print("What kind of level is that?!?!?! >:O")


    def makeBoard(self):
        # starts with board being printed in the terminal
        # self.board = [["O" for _ in range(self.boardRows)] for _ in range(self.boardCols)]
        # for x in self.board: # try to use 2 loops to print without list
        #     self.gameBoard = " ".join(x)
        #     print(self.gameBoard)
        for r in range(self.boardRows):
            for c in range(self.boardCols):
                self.dictBoard[(r, c)] = "O"
        self.countSpaces = (self.boardRows * self.boardCols)
        self.printBoard()
    
    def printBoard(self):
        for r in range(self.boardRows):
            for c in range(self.boardCols):
                print(self.dictBoard[(r,c)], end = " ")
            print()

    def userMove(self):
        # when coordinate is inputed (row x column) checks the space
        while True:
            self.user = input("Please enter a 'coordinate' to uncover a space or 'X, coordinate' to place or remove a flag: ").upper()
            self.user = self.user.translate(str.maketrans(string.punctuation, (" " * len(string.punctuation))))
            self.user = self.user.split()
            if len(self.user) == 2:
                try:
                    self.move = tuple(map(int, self.user))
                    if self.move in self.dictBoard:
                        break
                    else:
                        print("That's not even a space on the board >_>")
                except:
                    print("NO! >:O")
            elif len(self.user) == 3 and self.user[0] == "X":
                try:
                    self.flag = tuple(map(int, self.user[1:]))
                    if self.flag in self.dictBoard:
                        self.placeFlags()
                        break
                    else:
                        print("Sure. I can place a flag in the middle of nowhere for you! :D")
                except:
                    print("*BOOM* No flag for you! >:D")
            else:
                print("Invalid input.  Please try again.")

    def placeFlags(self):
        if self.countFlags <= self.numMines:
            if self.dictBoard[self.flag] == "O":
                self.dictBoard[self.flag] = "X"
                self.countFlags += 1
            elif self.dictBoard[self.flag] == "X":
                self.dictBoard[self.flag] = "O"
                self.countFlags -= 1
            else:
                pass

    def placeMines(self):
        # check how many mines we have placed
        while self.countMines < self.numMines:
            # randomly place the mines / find coordinates for row and colum
            mineRow = random.choice(range(self.boardRows))
            mineCols = random.choice(range(self.boardCols))
            coorMine = mineRow, mineCols
            # check if a mine is already there
            # if there is a mine already there, pass
            if (coorMine in self.dictSpace and self.dictSpace[coorMine] == "*") or coorMine == self.move:
                # print(self.countMines)
                pass
            # if the no mine / replace the space with mine
            # else:
            elif coorMine not in self.dictSpace or self.dictSpace[coorMine] != "*":
                self.dictSpace[coorMine] = "*"
                # if true will add a mine to the counter
                self.countMines += 1
                self.placeNums(mineRow, mineCols)

    # def printMines(self):
    #     print(self.dictSpace)

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
            elif space in self.dictSpace and self.dictSpace[space] != "*": #and self.dictSpace[space] != "M":
                self.dictSpace[space] += 1

    def checkMove(self):
        # if mine is there at coordinate - game over
        if self.dictBoard[self.move] == "O":
            if self.move in self.dictSpace:
                if self.dictSpace[self.move] != "*":
                    self.dictBoard[self.move] = self.dictSpace[self.move]
                    self.countSpaces -= 1
                    self.printBoard()
                else:
                    self.dictBoard[self.move] = self.dictSpace[self.move]
                    self.printBoard()
                    print("Game Over!")
                    exit()
            else:
                self.dictBoard[self.move] = " "
                self.countSpaces -= 1
                self.uncoverSpace(self.move[0], self.move[1])
                self.printBoard()
        elif self.dictBoard[self.move] != "O":
            print("You already uncovered this space -_-")
        elif self.dictBoard[self.flag] == "X":
            print("Uhmmm, you want to dig up a flag you put down??")
        elif self.dictBoard[self.flag] == "O":
            pass


    def uncoverSpace(self, row, col):
        spaceList = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        for space in spaceList:
            if space[0] < 0 or space[1] < 0 or space[0] > (self.boardRows - 1) or space[1] > (self.boardCols - 1):
                continue
            if self.dictBoard[space] == "O":
                if space not in self.dictSpace:
                    self.dictBoard[space] = " "
                    self.countSpaces -= 1
                    self.uncoverSpace(space[0], space[1])
                elif space in self.dictSpace and self.dictSpace[space] != "*":
                    self.dictBoard[space] = self.dictSpace[space]
                    self.countSpaces -= 1
                    
    def userWin(self):
        if self.countSpaces == self.numMines:
            print("Congrats you won! :D")
            exit()

    def gamePlay(self):
        self.userWin()
        self.userMove()
        self.checkMove()
        self.gamePlay()

    def startGame(self):
        self.chooseLevel()
        self.makeBoard()
        self.userWin()
        self.userMove()
        self.placeMines()
        self.checkMove()
        self.gamePlay()

minesweeper = Minesweeper()
minesweeper.startGame()
# minesweeper.chooseLevel()
# minesweeper.makeBoard()
# minesweeper.gamePlay()

# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!