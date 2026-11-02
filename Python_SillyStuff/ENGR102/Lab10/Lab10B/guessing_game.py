# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   guessing_game
# Date:         27 October 2026

def compare(a, secret):
    a = int(a)
    if a < secret:
        return -1
    elif a > secret:
        return 1
    elif a == secret:
        return 0

def isValid(input1):
    try:
        test = int(input1) < 10
        return True
    except:
        return False

secretNum = 27
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
guess = None; count = 0
while guess != str(secretNum):
    guess = input("What is your guess? ")
    if isValid(guess):
        if compare(guess, secretNum) == -1:
            print("Too low!")
            count += 1
        elif compare(guess, secretNum) == 1:
            print("Too high!")
            count += 1
        else:
            print(f"You guessed it! It took you {count} guesses.")
    else:
        guess = input("Bad input! Try again: ")
