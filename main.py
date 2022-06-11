import random
# where
# rock = R
# paper = P
# scissors = S

possible_options = ["rock", "paper", "scissors"]

while True:
    computer_option = random.choice(possible_options)
    user_option = input(
        "\nPick an option between (Rock, Paper and Scissors): ").lower()
    if (user_option == "rock" or user_option == "paper" or user_option == "scissors"):
        print(
            f"\nPlayer({user_option}) : CPU({computer_option}).\n")

    else:
        print("invalid")

    if user_option == computer_option:
        print(f"Both players selected {user_option}. Hence, it's a tie!")
    elif user_option == "rock":
        if computer_option == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_option == "paper":
        if computer_option == "rock":
            print("paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_option == "scissors":
        if computer_option == "paper":
            print("scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("\nPlay again? (y/n)\n: ")
    if play_again.lower() != "y":
        break
