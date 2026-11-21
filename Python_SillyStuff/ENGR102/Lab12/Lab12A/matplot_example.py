# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   matplot_example
# Date:         12 November 2026

# Imports
import matplotlib.pyplot as plt, numpy as np

# Plot 1        y = (x^2) / (4f)    -2.0 <= x <= 2.0; f = 2 & 6

# Create domain
x = np.linspace(-2, 2)
# Create the first graph
y = (x**2) / (4 * 2)
plt.plot(x, y, color="red", linewidth=2, label="f=2")
# Create the second graph
y = (x**2) / (4 * 6)
plt.plot(x, y, color="blue", linewidth=6, label="f=6")

# Format and display
plt.title("Parabola plots with varying focal length")
plt.xlabel("x"); plt.ylabel("y")
plt.legend(loc="lower left")
plt.show()

# Plot 2        y = 2x^3 + 3x^2 - 11x - 6        -4 <= x <= 4; 25 points
x = np.linspace(-4, 4, 25)
y = 2 * x**3 + 3 * x**2 - 11 * x - 6
plt.scatter(x, y, marker="*", color="yellow", edgecolors="black", s=100)

# Format and display
plt.title("Plot of cubic polynomial")
plt.xlabel("x values"); plt.ylabel("y values")
plt.show()

# Plot 3        y = cos(x) and sin(x)           -2PI <= x <= 2PI
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Create the cosine graph
plt.subplot(2, 1, 1)
y = np.cos(x)
plt.plot(x, y, label="cos(x)", color="maroon")
plt.ylabel("y=cos(x)"); plt.yticks(range(-1, 2))
plt.legend(loc="lower right"); plt.grid(True)

# Create the sine graph
plt.subplot(2, 1, 2)
y = np.sin(x)
plt.plot(x, y, label="sin(x)", color="gray")
plt.xlabel("x"); plt.ylabel("y=sin(x)"); plt.yticks(range(-1, 2))
plt.legend(loc="upper right"); plt.grid(True)

# Create the super title and display
plt.suptitle("Plot of cos(x) and sin(x)")
plt.show()
