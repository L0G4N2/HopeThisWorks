# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab8B-Act3
# Date:         14 October 2026

# Context for the user
print("This program requests a single number value from the user that states the number of usernames and passwords to be accepted.", end=" ")
print("The user is then prompted to enter a username and password combination until they have access to the system.")

# Retrieve the magic number from the user
num = int(input("Enter a positive integer to be used to determine the number of inputs for each username/password: "))

# Retrieve usernames
usernames = []
for i in range(num):
    temp = input("Enter a username: ")
    usernames.append(temp)

# Retrieve passwords
passwords = []
for i in range(num):
    temp = input("Enter a password: ")
    passwords.append(temp)

# Ask the user to enter a correct username/password combination
inputName = input("Enter a valid username: ")
inputPass = input("Enter a valid password: ")

# Check if the correct combination has been entered
isValid = False
while not(isValid):
    # Check if the username/password exist
    exists = False
    for name in usernames:
        if inputName == name:
            exists = True
            break
        else:
            exists = False
    for password in passwords:
        if inputPass == password:
            exists = True
            break
        else:
            exists = False

    # Check if the combination is correct
    if exists and (usernames.index(inputName) == passwords.index(inputPass)):
        isValid = True
    else:
        inputName = input("The previous combination was invalid. Enter a new username: ")
        inputPass = input("The previous combination was invalid. Enter a new password: ")

print("You have been granted access into the system!")
