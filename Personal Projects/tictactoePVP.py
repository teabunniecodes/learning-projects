# dictionary of the board spaces with the keys that will be pressed
theBoard = {
    1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "
}

theWins = [
    # horizantal win conditions
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

    # vertical win conditions
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    
    # diagonal win conditions
    [1, 5, 9],
    [3, 5, 7]
]

class tictactoe():
    def __init__(self):
        self.player = "X"
        self.turn = 0
        self.winner = False

    # set up and displays it when called
    def board(self):
        print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
        print("-+-+-")
        print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
        print("-+-+-")
        print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")

    # gives the parameters of a turn
    def turns(self):
        while self.turn < 9 and self.winner == False:
            # takes user input and checks that it is a valid input
            while True:
                try:
                    self.space = int(input(f"It is {self.player}'s turn. Please enter a number 1-9: "))
                    break
                except:
                    print(f"That's not a number between 1-9 Player {self.player}!!!! >:O")
            # checks if the board is empty in the space that the user has chosen
            if theBoard[self.space] == " " and self.space > 0 and self.space < 10:
                # places an X in the space if it is a valid input when it is X's turn
                if self.player == "X":
                    theBoard[self.space] = self.player
                    self.wins()
                    self.player = "O"
                    self.turn += 1
                # places an O in the space if it is a valid input when it is O's turn
                else:
                    theBoard[self.space] = self.player
                    self.wins()
                    self.player = "X"
                    self.turn += 1
            # if the space is not empty, notifies the user and asks for input again
            else:
                print(f"That space is already taken")

    # defines how to win the game and checks if met
    def wins(self):
        if any((theBoard[win[0]] != " ") and (theBoard[win[0]] == theBoard[win[1]] == theBoard[win[2]]) for win in theWins):
            print(f"Congrats {self.player} has won!")
            self.winner = True  

game = tictactoe()
game.board()
game.turns()
game.board()