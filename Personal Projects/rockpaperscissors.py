from pydoc import plain
import random

def is_win(player, opponent):
    if player == opponent:
        print("You tied!")
    elif (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == "p"):
        print("You won!")
    else:
        print("You lost :(")

while True:
    user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissor: ")
    if user == "r" or user == "p" or user == "s":
        computer = random.choice(['r', 'p', 's'])
        print(f"The computer played {computer}")
        is_win(user, computer)
        break
    else:
        print("Thats not a valid choice!!!! >:O Stop trying to cheat!!!")