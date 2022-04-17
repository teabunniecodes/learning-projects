# create a dictionary with keys 1-9 and " " as value
# display the game board "|" between each of the dictionary values
# loop to check if the space has been taken
# if space has not been taken then replace X or O in the dictionary
# if space has been taken display error message to user that space has already been taken

theBoard = {
1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "
}

print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
print(f"-+-+-")
print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
print(f"-+-+-")
print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")

turns = 0
while turns < 10:
    turns += 1
    for space in theBoard:
        x = int(input("Select a space 1-9: "))
        space = x
        if theBoard[x] == " " and x > 0 and x < 10:
            theBoard[x] = str(input("Are you X or O? "))
        else:
            print("This space has already been taken")
        print(f"{theBoard[1]}|{theBoard[2]}|{theBoard[3]}")
        print(f"-+-+-")
        print(f"{theBoard[4]}|{theBoard[5]}|{theBoard[6]}")
        print(f"-+-+-")
        print(f"{theBoard[7]}|{theBoard[8]}|{theBoard[9]}")
