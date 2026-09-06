import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")

while True:

    user = input("\nEnter rock, paper, scissors or exit: ").lower()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid choice! ❌")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a Tie! 🤝")

    elif (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win! 🎉")
        user_score += 1

    else:
        print("Computer Wins! 🤖")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

print("\n========== FINAL SCORE ==========")
print("Your Score:", user_score)
print("Computer Score:", computer_score)