# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab6A(alt)
# Date:         30 September 2026

# Test Cases:
# print(f"The coefficient for 'A' is: {userCoeffList[0]}") # Prints out the coefficient of 'A' as a float number
# print(f"The coefficient for 'B' is: {userCoeffList[1]}") # Prints out the coefficient of 'B' as a float number
# print(f"The coefficient for 'C' is: {userCoeffList[2]}") # Prints out the coefficient of 'C' as a float number
# print(f"The coefficient for 'D' is: {userCoeffList[3]}") # Prints out the coefficient of 'D' as a float number
# print(f"Is the starting bound at least a difference of 1? {x2 > x1 + 1}") # Returned a value of True or False based on the logic

# Cubic functions are defined as: y = Ax^3 + Bx^2 + Cx + D, where the values of the coeffiecients are real numbers
coeffList = ['A', 'B', 'C', 'D']
userCoeffList = []

# Retrieve values of the coeefficients from the user
for i in range(4):
    temp = float(input(f"Enter the value of the coefficient of {coeffList[i]} as a real number: "))
    userCoeffList.append(temp)

# Intermediate Value Theorem (IVT) states that if a function is continuous on a closed interval [a, b]
# and takes on different signs at the endpoints of the interval, then there exists at least one root in the interval.
# This program will use IVT to prove that at least one root exists in the interval [x1, x2] for the given cubic function.

# Retrive the interval from the user
print("Enter the interval that the root takes on.")
x1 = float(input("Enter the left endpoint of the interval (x1 < x2): "))
x2 = float(input("Enter the right endpoint of the interval (x2 > x1): "))

# Functions to evaluate the cubic function at a certain point
def evalFunc(x):
    return userCoeffList[0] * x**3 + userCoeffList[1] * x**2 + userCoeffList[2] * x + userCoeffList[3]

# Define the cubic function as f(x) or foX
fox1 = evalFunc(x1); fox2 = evalFunc(x2)

# Check if the function takes on different signs at the endpoints of the interval
if (fox1 < 0 and fox2 > 0) or (fox1 > 0 and fox2 < 0):
    print(f"The function takes on different signs at the endpoints of the interval [{x1}, {x2}].")
    print("Therefore, by the Intermediate Value Theorem, there exists at least one root in the interval.")

    # Use the Bisection method to find the root in the interval [x1, x2]
    a = x1; b = x2; c = (a + b) / 2
    iterations = 0
    while not (evalFunc(c) >= -1e-15 and evalFunc(c) <= 1e-15):
        if (evalFunc(c) < 0 and fox1 < 0) or (evalFunc(c) > 0 and fox1 > 0):
            a = c
        else:
            b = c
        c = (a + b) / 2
        iterations += 1
    print(f"The root in the interval [{x1}, {x2}] is approximately {c:.6f}.")
    print(f"Number of iterations: {iterations}")
else:
    print(f"The function does not take on different signs at the endpoints of the interval [{x1}, {x2}].")
    print("Therefore, we cannot conclude that there exists a root in the interval based on the Intermediate Value Theorem.")

# Optional Challenge, find the max and min values of the function
# Solve for the extreme values of the cubic function by using the discriminat of the derivative of the cubic function
# The derivative of the cubic function is a quadratic function, and the extreme values of the cubic function occur at the roots of its derivative
# The discriminant of the derivative is: (2B)^2 - 4(3AC) = 4B^2 - 12AC
def solveExtreme(A, B, C):
    # Calculate the discriminant
    discriminant = 4 * (B**2) - (12 * A * C)
    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        return [-B / (3 * A)]  # One real root
    else:
        root1 = (-2 * B + discriminant**0.5) / (6 * A)
        root2 = (-2 * B - discriminant**0.5) / (6 * A)
        return [root1, root2]  # Two real roots

print("------ Optional Challenge ------")
print(f"The extreme values of the function f(x) = {userCoeffList[0]}x^3 + {userCoeffList[1]}x^2 + {userCoeffList[2]}x + {userCoeffList[3]} are at x = {solveExtreme(userCoeffList[0], userCoeffList[1], userCoeffList[2])}")
