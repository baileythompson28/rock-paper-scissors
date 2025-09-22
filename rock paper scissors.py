import random

def get_user_move(round_num):
    """Prompt the user for a move for the given round. Returns 'r', 'p', 's' or None if invalid."""
    print(f"\nROUND {round_num}")
    move = input("Enter your move (r, p, s) -> ").lower()
    if move not in ("r", "p", "s"):
        print("Invalid input, round skipped.")
        return None
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_round_winner(user_move, comp_move):
    """Return 'user', 'comp', or 'tie' based on moves."""
    if user_move == comp_move:
        return "tie"
    if (user_move == "r" and comp_move == "s") or \
       (user_move == "p" and comp_move == "r") or \
       (user_move == "s" and comp_move == "p"):
        return "user"
    return "comp"

def print_round_result(user_move, comp_move, winner):
    moves_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    if user_move is None:
        return (0, 0)  # invalid round, no wins
    print(f"Computer chose: {comp_move}")
    print(f"You chose {moves_names[user_move]}, Computer chose {moves_names[comp_move]}")
    if winner == "tie":
        print("It's a tie!")
        return (0, 0)
    if winner == "user":
        print("You win!")
        return (1, 0)
    print("The computer wins!")
    return (0, 1)

def main():
    print("Welcome to a game of Rock, Paper, Scissors!")
    user_wins = 0
    comp_wins = 0

    for round_num in range(1, 6):
        user_move = get_user_move(round_num)
        if user_move is None:
            # invalid input counts as the round being skipped (no wins)
            continue
        comp_move = get_computer_move()
        winner = determine_round_winner(user_move, comp_move)
        u_inc, c_inc = print_round_result(user_move, comp_move, winner)
        user_wins += u_inc
        comp_wins += c_inc

    print("\nResults:")
    print(f"You won {user_wins} rounds.")
    print(f"The computer won {comp_wins} rounds.")
    print(f"Ties: {5 - (user_wins + comp_wins)}")

    if user_wins > comp_wins:
        print("You are the winner!")
    elif comp_wins > user_wins:
        print("The computer is the winner!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()
