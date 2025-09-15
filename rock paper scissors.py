import random

print("Welcome to a game of Rock, Paper, Scissors!")

user_wins = 0
comp_wins = 0

for round_num in range(1, 6):
    print(f"\nROUND {round_num}")
    my_move = input("Enter your move (r, p, s) -> ").lower()
    if my_move not in ("r", "p", "s"):
        print("Invalid input, round skipped.")
        continue

    comp_moves = ["r", "p", "s"]
    comp_move = random.choice(comp_moves)
    print(f"Computer chose: {comp_move}")

    moves_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    print(f"You chose {moves_names[my_move]}, Computer chose {moves_names[comp_move]}")

    if my_move == comp_move:
        print("It's a tie!")
    elif (my_move == "r" and comp_move == "s") or (my_move == "p" and comp_move == "r") or (my_move == "s" and comp_move == "p"):
        print("You win!")
        user_wins += 1
    else:
        print("The computer wins!")
        comp_wins += 1

print("\nSeries Results:")
print(f"You won {user_wins} rounds.")
print(f"The computer won {comp_wins} rounds.")
print(f"Ties: {5 - (user_wins + comp_wins)}")

if user_wins > comp_wins:
    print("You are the winner!")
elif comp_wins > user_wins:
    print("The computer is the winner!")
else:
    print("Tie!")