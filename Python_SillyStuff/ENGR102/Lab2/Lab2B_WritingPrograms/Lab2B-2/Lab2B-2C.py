# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Logan Gutierrez 737008832
# Section:      555
# Assignment:   2B-2C
# Date:         1 September 2026

import numpy as np

# Using this formula for each set of coordinates and time, we can calculate the position of the object at a given time between the two sets of coordinates and time.
# ((timeGiven - t1) * speed) + initialX

# First set of coordinates and time
x1 = 1
y1 = 3
z1 = 7
t1 = 13

# Second set of coordinates and time
x2 = 23
y2 = -5
z2 = 10
t2 = 84

# Time of interpolations
interpolation1 = 20
interpolation2 = 50

# It takes 4 jumps to get from 0 to 4
#       0 -> 1 -> 2 -> 3 -> 4
# But there are 5 points in total (0, 1, 2, 3, 4)
# So I'll divide the time difference by 4 to get the time step
# Difference between the two times then divide by 4 for even interpolation calculations
# The time interval is between 20 and 50
timeDiff = interpolation2 - interpolation1
timeStep = timeDiff / 4

# Calculate the speed of the object in each direction
speedX = (x2 - x1) / (t2 - t1)
speedY = (y2 - y1) / (t2 - t1)
speedZ = (z2 - z1) / (t2 - t1)

# Repeat the calculation for times 20 through 50 seconds evenly spaced out
for t in np.arange(interpolation1, interpolation2 + timeStep, timeStep):
    x3 = ((t - t1) * speedX) + x1
    y3 = ((t - t1) * speedY) + y1
    z3 = ((t - t1) * speedZ) + z1
    print(f"The position of the object at time {t} is: ({x3:.2f}, {y3:.2f}, {z3:.2f})")
    print("------------------")
