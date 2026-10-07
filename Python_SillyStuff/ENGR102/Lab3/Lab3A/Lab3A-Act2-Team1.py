# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
# Section:      555
# Assignment:   Lab3A-Act2
# Date:         10 September 2026

names = []
birthdays = []

numUsers = int(input("How many users' birthday's will be recorded (max: 4)? "))

for i in range(numUsers):
    name = input(f"Enter the name of user {i + 1} as (First, Last): ") 
    birthday = input("Enter your birthday as (mm, dd, yyyy): ")
    names.append(name)
    birthdays.append(birthday)

print("\tNames:\t|\tBirthdays:")
for i in range(len(names)):
    print(f"{names[i]}\t|   {birthdays[i]}")
