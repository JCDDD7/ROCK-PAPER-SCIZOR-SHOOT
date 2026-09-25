import random

player_choices = ["rock", "paper", "scissors"]

while True:
    choice = input(
        "Enter your choice (rock, paper, or scissors): ").strip().lower()

    if choice not in player_choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(player_choices)
    print(f"Computer chose: {computer_choice.title()}")

    if choice == computer_choice:
        print("It's a tie!")

    elif choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")

    elif choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")

    elif choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")

    else:
        print(f"Computer wins! {computer_choice.title()} beats {choice}.")

    play_again = input("Would you like to play again? (yes/no): ")
    play_again = play_again.strip().lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break