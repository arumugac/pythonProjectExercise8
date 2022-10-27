import random
UserScore = 0
CompScore = 0
while True:
    user = (input("Shall we play rock, paper,scissors select (y/n):\n "))
    if user == 'n':
        break
    else:
        if user == 'y':
            user = input("Enter your choice (rock, paper, scissors):")
            choices = ["rock", "paper", "scissors"]
            computer = random.choice(choices)
        else:
            if choices == ["0", "0", "0"]:
                print("Invalid Entry")

    print(f"\nYou chose {user}, computer chose {computer}.\n")
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
        (UserScore): int = 0
        (CompScore): int = 0

    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
            UserScore += 1
        else:
            print("Paper covers rock! You lose.")
            CompScore += 1
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
            UserScore += 1
        else:
            print("Scissors cuts paper! You lose.")
            CompScore += 1
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
            UserScore += 1
        else:
            print("Rock smashes scissors! You lose.")
            CompScore += 1
    print(f"Your Score = {UserScore}")
    print(f"Computer Score = {CompScore}")

    repeat = input("Play again? (y/n): ")
    if repeat.lower() != "y":
        break
