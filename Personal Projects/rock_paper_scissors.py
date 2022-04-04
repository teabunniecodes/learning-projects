from pydoc import plain
import random

user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissor: ")
computer = random.choice(['r', 'p', 's'])

print(f"The computer played {computer}")

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == "p"):
        return True

if user == computer:
    print("You tied!")

elif is_win(user, computer):
    print("You won!")

else:
    print("You lost :(")
