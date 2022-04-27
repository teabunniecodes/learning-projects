import random

moves = ['r', 'p', 's']

def is_win(player, opponent):
        if player == opponent:
            print("You tied!")
        elif (player == moves[0] and opponent == moves[2]) or (player == moves[1] and opponent == moves[0]) or (player == moves[2] and opponent == moves[1]):
            print("You won!")
        else:
            print("You lost :(")

while True:
    user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissor: ")
    if user in moves:
        computer = random.choice(moves)
        print(f"The computer played {computer}")
        is_win(user, computer)
        break
    else:
        print("Thats not a valid choice!!!! >:O Stop trying to cheat!!!")