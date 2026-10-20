# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   ascii_clock_LG
# Date:         14 October 2026

# Lists containing regular integer numbers and another containing the "ASCII Numbers"
asciiNumbersList = [["000", " 1 ", "222", "333", "4 4", "555", "666", "777", "888", "999"],
                    ["0 0", "11 ", "  2", "  3", "4 4", "5  ", "6  ", "  7", "8 8", "9 9"],
                    ["0 0", " 1 ", "222", "333", "444", "555", "666", "  7", "888", "999"],
                    ["0 0", " 1 ", "2  ", "  3", "  4", "  5", "6 6", "  7", "8 8", "  9"],
                    ["000", "111", "222", "333", "  4", "555", "666", "  7", "888", "  9"]
                    ]

# Test Case: Ensure that the list of "ASCII Numbers" are stored and formatted correctly for num in asciiNumbersList: print(num)

# Context for the user
print("This program will take a time input and display it in \"ASCII Numbers\". Time is printed in Military Time (24-hour format).", end=" ")
print("Do not enter any leading zeros for the hour. For example, enter 0:00 instead of 00:00 and minutes must be from 0-59.", end=" ")
print("The program will throw an error and end if the input either does not include a ':' or has more than one.", end=" ")
print("An error will also be thrown if there is no value before and/or after the colon.")

# Determine if the user has input a correct time format
time = ""; isValid = False
while not(isValid):
    # Take input of the time from the user as either 00:00 or 0:00
    time = list(input("Enter a time (either in the format of H:MM or HH:MM): "))
    indexColon = time.index(":") # Find the index of the colon
    hour = ""; minute = ""
    lenHour = 0; lenMinute = 0
    for i in range(len(time)):
        if i < indexColon:
            hour += time[i]
            lenHour += 1
        elif i > indexColon:
            minute += time[i]
            lenMinute += 1
    # Exit the loop if the hour and minutes are acceptable
    if (int(hour) < 25 and int(hour) > 0) and (int(minute) < 60 and int(minute) >= 0) and (lenHour == 1 or lenHour == 2) and (lenMinute == 2):
        isValid = True
    else:
        print("That was an invalid time. Please enter a valid time.")

# while len(time) != 4 and len(time) != 5:
#     print("Invalid input. Please enter a time in the format of H:MM or HH:MM.")
#     time = list(input("Enter a time (either in the format of H:MM or HH:MM): "))

# Convert the numerical values of the time to be integers and keep the colon as is
for t in time: # type: ignore
    if t != ":":
        time[time.index(t)] = int(t) # type: ignore

# Print out the input time as "ASCII Numbers"
for i in range(5):
    for j in range(len(time)):
        if (len(time) == 4 and j == 1) or (len(time) == 5 and j == 2):
            if i % 2 == 1:
                print(":", end=" ")
            else:
                print(" ", end=" ")
        else:
            print(asciiNumbersList[i][time[j]], end=" ") # type: ignore
    print()
