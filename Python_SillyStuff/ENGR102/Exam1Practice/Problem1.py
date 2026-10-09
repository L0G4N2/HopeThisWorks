# Write a Python program to take as input 5 birthdays from 5 users (1 each) and output them in chronological order.
# Dates should be entered with the month and day (not year) in the format "June 6" as a single input per user.
# You may format the output however you like (including using numbers for the month instead of words).
# This is a good problem to practice using lists of lists.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = []
for i in range(5):
    birthday = input (f"User {i + 1}, please enter your birthday (e.g., 'June 6'): ")
    temp = birthday.split()
    month = temp[0]
    day = int(temp[1])
    monthIndex = months.index(month) + 1
    days.append([monthIndex, day, birthday])

# Sort the birthdays chronologically
days.sort()

# Output the birthdays in chronological order
for monthIndex, day, birthday in days:
    print(f"{months[monthIndex - 1]} {day}")
