# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-2
# Date:         8 September 2026

from math import *

# List of algebraic characters
positionVars = ['x', 'y', 'z']

# Functions for vector calculation
def vectorLength(vector):
    length = 0
    for i in range(len(vector)):
        length += pow(vector[i], 2)
    return sqrt(length)

def normalize(vector):
    newVector = []
    for i in range(len(vector)):
        temp = vector[i] / vectorLength(vector)
        newVector.append(temp)
    return newVector

def dotProduct(vector1, vector2):
    temp = 0
    for i in range(len(positionVars)):
        temp += vector1[i] * vector2[i]
    return temp

def evalCosine(vector1, vector2):
    numerator = dotProduct(vector1, vector2)
    denominator = vectorLength(vector1) * vectorLength(vector2)
    return numerator / denominator

def evalTheta(vector1, vector2):
    return acos(evalCosine(vector1, vector2))

# Using this function instead of math.radians() due to a round-off error
def toDegrees(radians):
    return radians * (180 / pi)

# Retrieve the coordinates of the user
userPosition = []
for i in range(len(positionVars)):
    temp = float(input(f"Enter your {positionVars[i]}-position: "))
    userPosition.append(temp)

# Retrieve the coordinates of the first position observed
position1 = []
for i in range(len(positionVars)):
    temp = float(input(f"Enter the {positionVars[i]}-position of the first observation point: "))
    position1.append(temp)

# Retrieve the coordinates of the second position observed
position2 = []
for i in range(len(positionVars)):
    temp = float(input(f"Enter the {positionVars[i]}-position of the second observation point: "))
    position2.append(temp)

# Create vector from user to first position
vector1 = []
for i in range(len(position1)):
    temp = position1[i] - userPosition[i]
    vector1.append(temp)
vector1 = normalize(vector1)

# Create a vector from user to second position
vector2 = []
for i in range(len(position1)):
    temp = position2[i] - userPosition[i]
    vector2.append(temp)
vector2 = normalize(vector2)

# Solve for the angle between the first and second observed points
print(f"The angle between the first and second points of observation is: {toDegrees(evalTheta(vector1, vector2))}")
