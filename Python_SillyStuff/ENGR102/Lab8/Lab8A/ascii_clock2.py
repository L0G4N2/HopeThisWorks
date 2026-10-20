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

# The list containing containing the "ASCII Numbers"
asciiNumbersList = [["000", " 1 ", "222", "333", "4 4", "555", "666", "777", "888", "999"],
                    ["0 0", "11 ", "  2", "  3", "4 4", "5  ", "6  ", "  7", "8 8", "9 9"],
                    ["0 0", " 1 ", "222", "333", "444", "555", "666", "  7", "888", "999"],
                    ["0 0", " 1 ", "2  ", "  3", "  4", "  5", "6 6", "  7", "8 8", "  9"],
                    ["000", "111", "222", "333", "  4", "555", "666", "  7", "888", "  9"]
                   ]

# Test Case: Ensure that the list of "ASCII Numbers" are stored and formatted correctly
    # for num in asciiNumbersList:
    #     print(num)

# Context for the user
print("This program will take a time input and display it in \"ASCII Numbers\". Time is printed in Military Time (24-hour format).", end=" ")
print("Do not enter any leading zeros for the hour. For example, enter 0:00 instead of 00:00 and minutes must be from 0-59.", end=" ")
print("The program will throw an error and end if the input either does not include a ':' or has more than one.", end=" ")
print("An error will also be thrown if there is no value before and/or after the colon.")

# Determine if the user has input a correct time format
time = ""; isValid = False
while not(isValid):
    # Take input of the time from the user as either 00:00 or 0:00
    time = input("Enter a time (either in the format of H:MM or HH:MM): ")
    split = time.split(":")
    isValidHour = (int(split[0]) > 0 and int(split[0]) < 24 and len(split[0]) == 1) or ((len(split[0]) == 2 and ((int(split[0]) > 0) and split[0][0] != "0") or int(split[0]) == 0))
    isValidMinute = len(split[1]) == 2 and int(split[1]) >= 0 and int(split[1]) <= 59 
    if isValidHour and isValidMinute:
        time = list(time)
        isValid = True
    else:
        print("That was an invalid time. Please enter a valid time.")

# Convert the numerical values of the time to be integers and keep the colon as is
for t in time: # type: ignore
    if t != ":":
        time[time.index(t)] = int(t) # type: ignore

# Print out the input time as "ASCII Numbers"
for row in range(5):
    for column in range(len(time)):
        if (len(time) == 4 and column == 1) or (len(time) == 5 and column == 2):
            if row % 2 == 1:
                print(":", end=" ")
            else:
                print(" ", end=" ")
        else:
            print(asciiNumbersList[row][time[column]], end=" ") # type: ignore
    print()
