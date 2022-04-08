theBoard = {
    1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "
}

class tictactoe():
    def __init__(self):
        self.player = "X"
        self.turn = 0
        self.winner = False

    def board(self):
        print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
        print("-+-+-")
        print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
        print("-+-+-")
        print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")

    def turns(self):
        while self.turn < 9 and self.winner == False:
            self.space = int(input("Please enter a number 1-9: "))
            if theBoard[self.space] == " " and self.space > 0 and self.space < 10:
                if self.player == "X":
                    theBoard[self.space] = self.player
                    self.wins()
                    self.player = "O"
                    self.turn += 1
                else:
                    theBoard[self.space] = self.player
                    self.wins()
                    self.player = "X"
                    self.turn += 1
            else:
                print(f"That space is already taken")

    def wins(self):
        if (theBoard[1] == theBoard [2] == theBoard [3]) and theBoard[1] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[1] == theBoard[4] == theBoard[7]) and theBoard[1] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[1] == theBoard[5] == theBoard[9]) and theBoard[1] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[2] == theBoard[5] == theBoard[8]) and theBoard[2] != " ":
            self.winner = True  
            print(f"Congrats {self.player} has won!")
        elif (theBoard[3] == theBoard[6] == theBoard[9]) and theBoard[3] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[3] == theBoard[5] == theBoard[7]) and theBoard[3] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[4] == theBoard[5] == theBoard[6]) and theBoard[4] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")
        elif (theBoard[7] == theBoard[8] == theBoard[9]) and theBoard[7] != " ":
            self.winner = True
            print(f"Congrats {self.player} has won!")                

game = tictactoe()
game.board()
game.turns()
game.board()