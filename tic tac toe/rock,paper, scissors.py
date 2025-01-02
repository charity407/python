import random

user_wins = 0
computer_wins = 0

# Options for the game
options = ["rock", "paper", "scissors"]

while True:
    # Get user input
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()

    if user_input == "q":  # Exit the game
        break

    if user_input not in options:  # Check valid input
        print("Invalid input. Please try again!")
        continue

    # Generate computer's choice
    random_number = random.randint(0, 2)  # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    # Determine the winner
    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("Computer wins!")
        computer_wins += 1

    # Print current score
    print(f"Score: You {user_wins} - {computer_wins} Computer\n")

# Final score after quitting
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")

    







 