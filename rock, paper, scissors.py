import random

print("Welcome to a game of Rock, Paper, Scissors!")
my_move = input("Enter your move (r, p, s) -> ").lower()

# rock = "r"
# paper = "p" 
# scissors = "s"

#user turn
if my_move in ('r', 'p', 's'):
    print("Good move! It's now the computers turn!")
else:
    print("Invalid input")

#computer turn
comp_moves = ["r", "p", "s"]
comp_move = random.choice(comp_moves)
print(f"Computer chose: {comp_move}")

#putting into words
moves_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
print(f"You chose {moves_names[my_move]}, Computer chose {moves_names[comp_move]}")

#determine winner
if my_move == comp_move:
    print("It's a tie!")
elif (my_move == "r" and comp_move == "s") or (my_move == "p" and comp_move == "r") or (my_move == "s" and comp_move == "p"):
    print("You win!")
else:
    print("The computer wins!")



