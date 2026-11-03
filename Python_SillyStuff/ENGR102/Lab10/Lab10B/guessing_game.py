# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   guessing_game
# Date:         27 October 2026

# Comparison function that returns -1 if the guess is too low, 1 if it's too high, and 0 if it's correct
def compare(a, secret):
    a = int(a)
    if a < secret:
        return -1
    elif a > secret:
        return 1
    elif a == secret:
        return 0

# Function to check if the input is a valid integer by checking if it can be converted to an integer and is between 0 and 100 inclusive
def isValid(input1):
    try:
        test = 0 <= int(input1) <= 100
        return test
    except:
        return False

# Create a secret number and prompt the user to guess it
secretNum = 27
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
guess = input("What is your guess? "); count = 1

# Prompt the user for a new guess until they guess the correct number and only count valid guesses
while guess != str(secretNum):
    if isValid(guess):
        if compare(guess, secretNum) == -1:
            print("Too low!")
            count += 1
            guess = input("What is your guess? ")
        elif compare(guess, secretNum) == 1:
            print("Too high!")
            count += 1
            guess = input("What is your guess? ")
        else:
            break
    else:
        guess = input("Bad input! Try again: ")
print(f"You guessed it! It took you {count} guess(es).")
