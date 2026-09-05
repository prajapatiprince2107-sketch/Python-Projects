import random

secret_number = random.randint(1, 100)

attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100!")

while True:

    try:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("Too Low! 📉")

        elif guess > secret_number:
            print("Too High! 📈")

        else:
            print("\nCorrect! 🎉")
            print("You guessed the number in", attempts, "attempts.")
            break

    except ValueError:
        print("Please enter a valid number! ❌")