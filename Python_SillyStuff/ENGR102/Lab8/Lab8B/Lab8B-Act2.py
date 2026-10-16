# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab8B-Act2
# Date:         14 October 2026

from math import *

# List of axes
axes = ['x', 'y', 'z']

# Context for the user
print("This program takes an input of two vectors of either dimension specified by the user and returns the following calculations: ")
print("The magnitude of the vectors, A + B, A - B, and the dot product of the vectors")

# Retrieve the vector dimensions
dimension1 = int(input("What dimension is the first vector in? (2 or 3): "))
dimension2 = int(input("What dimension is the second vector in? (2 or 3): "))

# List of vectors
vector1 = []; vector2 = []

# Retrieve the vector values
for i in range(dimension1):
    temp = float(input(f"Enter the {axes[i]}-value of the first vector: "))
    vector1.append(temp)
for i in range(dimension2):
    temp = float(input(f"Enter the {axes[i]}-value of the second vector: "))
    vector2.append(temp)

# Convert the 2D vector to a 3D vector if at least one of them is a 3D vector
if len(vector1) >= len(vector2):
    vector2.append(0)
    print("Vector 2 has been converted to a 3D vector to perform the following calculations.")
elif len(vector2) >= len(vector1):
    vector1.append(0)
    print("Vector 1 has been converted to a 3D vector to perform the following calculations.")

# Calculate the magnitude of each vector
magnitude1 = 0
for i in range(len(vector1)):
    magnitude1 += vector1[i] ** 2
magnitude1 = sqrt(magnitude1)
print(f"The magnitude of vector 1 <{", ".join(map(str, vector1))}> is: {magnitude1}")

magnitude2 = 0
for i in range(len(vector2)):
    magnitude2 += vector2[i] ** 2
magnitude2 = sqrt(magnitude2)
print(f"The magnitude of vector 2 <{", ".join(map(str, vector2))}> is: {magnitude2}")

# Add the two vectors together
vectorSum = []
for i in range(len(vector1)):
    temp = vector1[i] + vector2[i]
    vectorSum.append(temp)
print(f"The sum of the two vectors creates the vector: <{", ".join(map(str, vectorSum))}>")

# Subtract Vector B from Vector A
vectorDiff = []
for i in range(len(vector1)):
    temp = vector1[i] - vector2[i]
    vectorDiff.append(temp)
print(f"Subtracting Vector B from Vector A creates the vector: <{", ".join(map(str, vectorDiff))}>")

# Take the dot product of the two vectors
vectorPro = 0
for i in range(len(vector1)):
    vectorPro += vector1[i] * vector2[i]
print(f"The dot product of the two vectors is: {vectorPro}")
