import random

def get_computer_choice():
    number = random.randint(0, 2)
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

user_choice = input("Enter your choice (rock, paper, or scissors): ").lower().strip()
computer_choice = get_computer_choice()
print(f"Computer chose: {computer_choice}")

winner = decide_winner(user_choice, computer_choice)
if winner == "draw":
    print("It's a draw!")
else:
    print(f"The winner is: {winner}!")
