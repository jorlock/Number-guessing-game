# Number Guesser - Version 2
# 25 NOV 2024
# Evan Sunil

import random

# Target variable to store a random target number for the user to guess
target = random.randint(1, 100)

# Controls whether while loop runs. Repeat until user guesses correct number
run_loop = True

while run_loop:

    # Guess variable to store the user's guess number
    guess = int(input("please guess the number(1-100): "))

    while not (guess >= 1 and guess <= 100):
        guess = int(input("That is not a valid number. Please guess between 1 and 100: "))

    if guess < target:  # Check whether the user's guess is less than the target
        print("your guess was too low")
    elif guess > target:  # Check whether the user's guess is greater than the target
        print("your guess was too high")
    elif guess == target:  # Check for correct guess
        # Stop repeating loop
        run_loop = False

# When user has guessed the correct answer
print("congratulations! you got the number")
