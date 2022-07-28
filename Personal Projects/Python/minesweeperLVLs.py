__author__ = 'ambivalentbunnie'

import random
import string

# echo -e "\e[1;33;40m Yellow on black \e[m"

class Minesweeper:
    # build board and define how many mines/level
    def __init__(self):
        self.dict_board = {}
        self.dict_space = {}
        self.count_mines = 0
        self.count_flags = 0
        self.board_rows = 0
        self.board_cols = 0
        self.num_mines = 0

    def get_level(self):
        choice = input("Please choose a level (Beginner, Intermediate, Advanced, Custom): ").lower()
        return choice

    def define_level(self):
        while True:
            level = ["beginner", "intermediate", "advanced", "custom"]
            choice = self.get_level()
            if choice in level:
                # beginner = 9x9 w/ 10 mines
                if choice == level[0]:
                    self.board_rows = 9
                    self.board_cols = 9
                    self.num_mines = 10
                    break
                # intermediate = 16x16 w/ 40 mines
                elif choice == level[1]:
                    self.board_rows = 16
                    self.board_cols = 16
                    self.num_mines = 40
                    break
                # advanced = 30x16 w/ 99 mines
                elif choice == level[2]:
                    self.board_rows = 16
                    self.board_cols = 30
                    self.num_mines = 99
                    break
                # custom = user inputs their custom level
                elif choice == level[3]:
                    while True:
                        try:
                            ### This causes the program to go on forever placing bombs :(
                            self.board_rows = int(input("Please enter a number 1-80 for rows: "))
                            self.board_cols = int(input("Please enter a number 1-80 for columns: "))
                            self.num_mines = int(input("Please enter a number 1-99 for bombs: "))
                            if 0 < self.board_rows <= 80 and 0 < self.board_cols <= 80 and 0 < self.num_mines <= 99 and self.num_mines < (self.board_rows * self.board_cols) / 2:
                                break
                            else: 
                                print("Can't make a board like that! D:")
                        except:
                            print("Can't make a board like that! D:")
                    break
            else:
                print("What kind of level is that?!?!?! >:O")

    def make_board(self):
        # starts with board being printed in the terminal
        # self.board = [["O" for _ in range(self.boardRows)] for _ in range(self.boardCols)]
        # for x in self.board: # try to use 2 loops to print without list
        #     self.gameBoard = " ".join(x)
        #     print(self.gameBoard)
        for r in range(self.board_rows):
            for c in range(self.board_cols):
                self.dict_board[(r, c)] = "O"
        self.countSpaces = (self.board_rows * self.board_cols)
        self.print_board()
    
    def print_board(self):
        for r in range(self.board_rows):
            for c in range(self.board_cols):
                print(self.dict_board[(r,c)], end = " ")
            print()

    def get_user_move(self):
        # when coordinate is inputed (row x column) checks the space
        self.user = input("Please enter a 'coordinate' to uncover a space or 'X, coordinate' to place or remove a flag: ").upper()
        self.user = self.user.translate(str.maketrans(string.punctuation, (" " * len(string.punctuation))))
        self.user = self.user.split()

    def make_move(self):
        while True:
            self.get_user_move()
            # determines if the user is inputting a space
            if len(self.user) == 2:
                try:
                    self.move = tuple(map(int, self.user))
                    if self.move in self.dict_board:
                        self.is_flagging = False
                        break
                    else:
                        print("That's not even a space on the board >_>")
                except:
                    print("NO! >:O")
            # determines if a user is inputting a flag
            elif len(self.user) == 3 and self.user[0] == "X":
                try:
                    self.flag = tuple(map(int, self.user[1:]))
                    if self.count_mines == 0:
                        print("You really want to place a flag on your first move?")
                    elif self.flag in self.dict_board:
                        self.place_flag()
                        self.is_flagging = True
                        break
                    else:
                        print("Sure. I can place a flag in the middle of nowhere for you! :D")
                except:
                    print("*BOOM* No flag for you! >:D")
            else:
                print("Invalid input.  Please try again.")

    def place_flag(self):
        if self.count_flags <= self.num_mines:
            if self.dict_board[self.flag] == "O":
                self.dict_board[self.flag] = "X"
                self.count_flags += 1
                self.print_board()
            elif self.dict_board[self.flag] == "X":
                self.dict_board[self.flag] = "O"
                self.count_flags -= 1
                self.print_board()
            else:
                print("You want to waste flag on a space you already uncovered??? o_O")

    def place_mines(self):
        # check how many mines we have placed
        while self.count_mines < self.num_mines:
            # randomly place the mines / find coordinates for row and colum
            mine_row = random.choice(range(self.board_rows))
            mine_cols = random.choice(range(self.board_cols))
            coor_mine = mine_row, mine_cols
            # check if a mine is already there
            # if there is a mine already there, pass
            if (coor_mine in self.dict_space and self.dict_space[coor_mine] == "*") or coor_mine == self.move:
                # print(self.countMines)
                pass
            # if the no mine / replace the space with mine
            # else:
            elif coor_mine not in self.dict_space or self.dict_space[coor_mine] != "*":
                self.dict_space[coor_mine] = "*"
                # if true will add a mine to the counter
                self.count_mines += 1
                self.place_nums(mine_row, mine_cols)

    # def printMines(self):
    #     print(self.dictSpace)

    # method will use the coordinates of the mines that are placed
    def place_nums(self, row, col):
        # finds coordinate of top left, top center, top right, left side, right side, bottom left, bottom center, bottom right surrounding the mine
        spaceList = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        # goes through the coordinates one by one
        for space in spaceList:
            # checks to see if the coordinate is a valid coordinate on the board - skips it if it is not
            if space[0] < 0 or space[1] < 0 or space[0] > (self.board_rows - 1) or space[1] > (self.board_cols - 1):
                continue
            # if the coordinate is not in the dictionary yet, adds key and value
            if space not in self.dict_space:
                self.dict_space[space] = 1
            # if the coordinate is already a key, increments the value up by 1
            elif space in self.dict_space and self.dict_space[space] != "*": #and self.dictSpace[space] != "M":
                self.dict_space[space] += 1

    def check_move(self):
        if self.is_flagging == False:
        # if mine is there at coordinate - game over
            if self.dict_board[self.move] == "O":
                if self.move in self.dict_space:
                    if self.dict_space[self.move] != "*":
                        self.dict_board[self.move] = self.dict_space[self.move]
                        self.countSpaces -= 1
                        self.print_board()
                    else:
                        self.dict_board[self.move] = self.dict_space[self.move]
                        self.print_board()
                        print("Game Over!")
                        exit()
                else:
                    self.dict_board[self.move] = " "
                    self.countSpaces -= 1
                    self.uncover_space(self.move[0], self.move[1])
                    self.print_board()
            elif self.dict_board[self.move] == "X":
                print("Uhmmm, you want to dig up a flag you put down??")
            elif self.dict_board[self.move] != "O":
                print("You already uncovered this space -_-")


    def uncover_space(self, row, col):
        spaceList = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        for space in spaceList:
            if space[0] < 0 or space[1] < 0 or space[0] > (self.board_rows - 1) or space[1] > (self.board_cols - 1):
                continue
            if self.dict_board[space] == "O":
                if space not in self.dict_space:
                    self.dict_board[space] = " "
                    self.countSpaces -= 1
                    self.uncover_space(space[0], space[1])
                elif space in self.dict_space and self.dict_space[space] != "*":
                    self.dict_board[space] = self.dict_space[space]
                    self.countSpaces -= 1
                    
    def user_win(self):
        if self.countSpaces == self.num_mines:
            print("Congrats you won! :D")
            exit()

    def game_play(self):
        self.user_win()
        self.make_move()
        self.check_move()
        self.game_play()

    def start_game(self):
        self.define_level()
        self.make_board()
        self.make_move()
        self.place_mines()
        self.check_move()
        self.game_play()

minesweeper = Minesweeper()
minesweeper.start_game()
# minesweeper.chooseLevel()
# minesweeper.makeBoard()
# minesweeper.gamePlay()

# print out the board again so user can see what is available
# when all the blank spaces are uncovered - winner is pronounced!