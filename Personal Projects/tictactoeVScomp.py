import random

theBoard = {
1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "
}
theWins = [
    # horizantal wins
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

    # vertical wins
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],

    # diagonal wins
    [1, 5, 9],
    [3, 5, 7],
]

class TicTacToe:
    def __init__(self):
        self.turns = 0
        self.player = "X"
        self.computer = "O"
        self.win = False

    def makeBoard(self):       
        print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
        print(f"-+-+-")
        print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
        print(f"-+-+-")
        print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")

    def getMove(self):
        # define when it is the players turn
        while True:
            try:
                self.move = int(input("Please choose a space 1-9: "))
                # check to make sure the space is not taken
                if self.move > 0 and self.move < 10 and theBoard[self.move] == " ":
                    theBoard[self.move] = self.player
                    break
                elif theBoard[self.move] != " ":
                    print("This space has already been taken")
            except:
                print("Stop cheating you cheater! >:O!!!!!!!")

    def getCompmove(self):
        # define when the computer moves
        self.compMove = random.choice(range(1,9))
        if theBoard[self.compMove] == " ":
            print(f"The computer chose {self.compMove}")
            theBoard[self.compMove] = self.computer
        else:
            self.getCompmove()

    def addTurns(self):
        self.turns += 1
        print(f"This was turn {self.turns}")     

    def isTurn(self):
        while self.turns < 9 and self.win == False:
            if self.turns % 2 == 0:
                self.getMove()
            elif self.turns % 2 == 1:
                self.getCompmove()
            self.addTurns()
            self.getWin()


    def getWin(self):
        for win in theWins:
            if (theBoard[win[0]] == theBoard[win[1]] == theBoard[win[2]]) and theBoard[win[0]] != " ":
                self.win = True
                self.makeBoard()
                print(f"Player {theBoard[win[0]]} has won!")

tictactoe = TicTacToe()
tictactoe.makeBoard()
tictactoe.isTurn()