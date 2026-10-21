# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   ascii_clock_ZA
# Date:         14 October 2026

# Determine if the user has input a correct time format
time = ""; isValid = False
while not(isValid):
    # Take input of the time from the user as either 00:00 or 0:00
    time = input("Enter a time (either in the format of H:MM or HH:MM): ")
    split = time.split(":")
    isValidHour = (int(split[0]) > 0 and int(split[0]) < 24 and len(split[0]) == 1) or ((len(split[0]) == 2 and ((int(split[0]) > 0) and int(split[0]) < 24 and split[0][0] != "0") or int(split[0]) == 0))
    isValidMinute = len(split[1]) == 2 and int(split[1]) >= 0 and int(split[1]) <= 59 
    if isValidHour and isValidMinute:
        time = list(time)
        isValid = True
    else:
        print("That was an invalid time. Please enter a valid time.")
