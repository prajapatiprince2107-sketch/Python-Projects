secret_number = 25
attempts = 0

print("🎮 Number Guessing Game")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("🎉 Correct!")
        print("Attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")