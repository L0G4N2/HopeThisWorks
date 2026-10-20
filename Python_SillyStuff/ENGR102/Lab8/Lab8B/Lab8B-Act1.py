# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab8B-Act1
# Date:         14 October 2026

# List of vowels including 'y'
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

# Context for the user
print("This program converts English words to 'Pig Latin' by moving the first letter to the end if it is a consonant and add 'ay'", end=' ')
print("at the end. It does not add the first letter to the end if it is a vowel, but it still adds 'ay' to the end.")
print("The program runs continuously and ends when the word 'stop' is input by the user.")

# Take a user input of a single word
word = input("Enter a single word to convert to 'Pig Latin': ").lower()
while word != 'stop':
    charList = list(word) # Store the individual charaters of the word in a list
    isVowel = False

    for char in word:
        # Check if the first word is a vowel
        for vowel in vowels:
            if charList[0] == vowel:
                isVowel = True
        # Convert the word to Pig Latin
        if isVowel:
            charList.append("ay")
            break
        else:
            temp = charList.pop(0)
            charList.append(temp)
    # Print the new word and ask for the next input
    for vowel in vowels:
        if vowel == word[0]:
            charList.pop()
            charList.append("yay")
            break
    print("".join(charList))
    word = input("Enter a new single word and enter 'stop' to stop the loop: ").lower()
