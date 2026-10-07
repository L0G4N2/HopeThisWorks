# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Logan Gutierrez 737008832
# Section:      555
# Assignment:   2B-2B
# Date:         1 September 2026

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

# Calculate the speed of the object in each direction (speed = distance / time)
speedX = (x2 - x1) / (t2 - t1)
speedY = (y2 - y1) / (t2 - t1)
speedZ = (z2 - z1) / (t2 - t1)

# Repeat the calculation for times: 50, 51, 52, 53, and 54
for t in range(50, 55, 1):
    x3 = ((t - t1) * speedX) + x1
    y3 = ((t - t1) * speedY) + y1
    z3 = ((t - t1) * speedZ) + z1
    print(f"The position of the object at time {t} is: ({x3:.2f}, {y3:.2f}, {z3:.2f})")
    print("------------------")
