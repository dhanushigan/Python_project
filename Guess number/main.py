# This is a guess-the-number game where the user has to guess the number correctly
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, your guess is too high.")
        elif guess < random_number:
            print("Sorry, your guess is too low.")
    print(f"Yay, you guessed the correct number: {random_number}!")

guess(10)

