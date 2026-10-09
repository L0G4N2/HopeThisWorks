secretWord = input("Enter a secret word (min. 6 characters): ")
while len(secretWord) < 6:
    secretWord = input("The secret word must be at least 6 characters long. Please enter a new secret word: ")

guess = input("Guess a letter: ")
count = 0
isCorrect = True
while isCorrect:
    count += 1
    for letter in secretWord:
        if guess == letter:
            guess = input("Guess another letter: ")
            break
            # isCorrect = False
            # break
print(f"The secret word is: \"{secretWord}\". You took {count} guesses!")
