import random

print("Welcome to Rock - Paper - Scissors Game")

user_score = 0
comp_score = 0

while True:
    print("\nOptions: rock | paper | scissors")
    user = input("Enter your choice: ").lower()
    choices = ["rock", "paper", "scissors"]

    if user not in choices:
        print("Invalid choice, please try again.")
        continue

    comp = random.choice(choices)
    print("You chose:", user)
    print("Computer chose:", comp)

    if user == comp:
        print("It's a tie.")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        comp_score += 1

    print("Score -> You:", user_score, "| Computer:", comp_score)

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\nFinal Score:")
        print("You:", user_score, "| Computer:", comp_score)
        print("Thanks for playing!")
        break
