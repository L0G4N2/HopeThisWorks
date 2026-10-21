# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   ascii_clock_DV
# Date:         14 October 2026

#temp variables before coming together in the final code
asciiNumbersList = []
time = []

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
