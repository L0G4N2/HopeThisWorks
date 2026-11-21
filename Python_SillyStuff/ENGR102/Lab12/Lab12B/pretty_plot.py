# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   pretty_plot
# Date:         15 November 2026

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Point A (used to start the program and then be replaced with other points to plot)
pointA = np.array([[0],
                   [1]
                  ])

# Matrix A (multiplied with Point A to determine the other 250 points to be plotted)
matrixA = np.array([[1.02, 0.095],
                    [-0.095, 1.02]
                   ])
plt.scatter(pointA[0, 0], pointA[1, 0], s=10)
for i in range(250):
    pointA = np.dot(matrixA, pointA)
    plt.scatter(pointA[0, 0], pointA[1, 0], s=10)

plt.xlabel("x"); plt.ylabel("y")
plt.title("Rainbow spiral")
plt.show()
