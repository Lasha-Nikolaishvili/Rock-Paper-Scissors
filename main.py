import random


def determine_winner(comp_c, pl_c):
    if comp_c == "Rock" and pl_c == "Paper":
        return "Player Won"
    elif comp_c == "Paper" and pl_c == "Rock":
        return "Computer Won"
    elif comp_c == "Rock" and pl_c == "Scissors":
        return "Computer Won"
    elif comp_c == "Scissors" and pl_c == "Rock":
        return "Player Won"
    elif comp_c == "Scissors" and pl_c == "Paper":
        return "Computer Won"
    elif comp_c == "Paper" and pl_c == "Scissors":
        return "Player Won"
    else:
        return "Tie"


options = ["Rock", "Paper", "Scissors"]
play_again = ""
print("The player who will reach 5 points first wins the game.")
print("Let's play Rock, Paper, Scissors!")

while play_again != "No":
    pl_points, comp_points = 0, 0

    while pl_points < 5 and comp_points < 5:
        user_choice = input("Players choice: ").capitalize()

        comp_choice = random.choice(options)
        print(f"The computers({comp_points}) choice: {comp_choice}")
        print(f"Players({pl_points}) choice: {user_choice}")
        result = determine_winner(comp_choice, user_choice)

        if result == "Player Won":
            pl_points += 1
        elif result == "Computer Won":
            comp_points += 1
        else:
            pass

        print(f"Result: {result}")

    if pl_points == 5:
        print("The player won!")
    else:
        print("The computer won!")
    play_again = input(f"Would you like to play again? ").capitalize()
