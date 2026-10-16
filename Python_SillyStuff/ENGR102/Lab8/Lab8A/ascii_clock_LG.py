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

# Take input of the time from the user as either 00:00 or 0:00
time = list(input("Enter a time (either in the format of 00:00 or 0:00): "))

# Convert the numerical values of the time to be integers and keep the colon as is
for t in time:
    if t != ":":
        time[time.index(t)] = int(t) # type: ignore
