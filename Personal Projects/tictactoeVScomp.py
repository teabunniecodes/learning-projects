# create the dictionary for the board
# create a class for the main game
# make the board
# check to make sure the space is not taken
    # define when it is the players turn (every odd move)
        # get user input for the chosen move
        # place "X" on the board
    # define when the computer moves
        # which will be every even move
        # place "O" on the board

theBoard = {
1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "
}

print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
print(f"-+-+-")
print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
print(f"-+-+-")
print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")
