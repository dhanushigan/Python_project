# This is guessing number game wher computer has to find the user guess

import random

def computer_guess(x):
    high = x
    low  = 1
    feedback = ""
    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} is too high(H) or too low (L) or correct (c)").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
    print(f"Yay the computer guess the correct number")

computer_guess(100)


