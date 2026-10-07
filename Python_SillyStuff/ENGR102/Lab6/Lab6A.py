# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab6A-Act1
# Date:         29 September 2026

# A useful library that allows us to perform calculus in the program
from sympy import *

# Variables to be used in the cubic function
x = symbols('x')
y = symbols('y')

# Cubic functions are defined as: y = Ax^3 + Bx^2 + Cx + D, where the values of the coeffiecients are real numbers
coeffList = ['A', 'B', 'C', 'D']
userCoeffList = []

# Retrieve values of the coeefficients from the user
for i in range(4):
    temp = float(input(f"Enter the value of the coefficient of {coeffList[i]} as a real number: "))
    userCoeffList.append(temp)

# Defining the cubic function as f(x) or foX
foX = (userCoeffList[0] * x**3) + (userCoeffList[1] * x**2) + (userCoeffList[2] * x) + userCoeffList[3]
eqFoX = Eq(foX, y).subs(y, 0)

# Solve for the roots of the given function
rootsFoX = solve(eqFoX, x)
print(f"The roots of the function f(x) = {foX} are: {rootsFoX}")

# Solve for the roots of the given function on a given interval using Bisection
x1 = float(input("Enter the first interval of the function as a real number: "))
x2 = float(input("Enter the second interval of the function as a real number greater than the first interval: "))

a = x1
b = x2
c = -1
iterations = 0
root1 = None
while not (foX.subs(x, c) >= -1e-15 and foX.subs(x, c) <= 1e-15):
    c = (a + b) / 2
    if foX.subs(x, c) >= -1e-15 and foX.subs(x, c) <= 1e-15:
        root1 = c
    elif (foX.subs(x, c) < 0 and foX.subs(x, a) < 0) or (foX.subs(x, c) > 0 and foX.subs(x, a) > 0):
        a = c
    elif (foX.subs(x, c) < 0 and foX.subs(x, b) < 0) or (foX.subs(x, c) > 0 and foX.subs(x, b) > 0):
        b = c
    iterations += 1
root1 = c
print(f"After {iterations} iterations, the root on the interval from x = {x1} to x = {x2} is: {root1}")

# Optional Challenge, find the max and min values of the function
# It is known that the derivative at these max and mins is equal to 0
# Therefore, if we differentiate the function and solve for x, those returned values will be the locations of the min and max
dFoX = diff(foX)
eqDfoX = Eq(dFoX, y).subs(y, 0)

# Find the extreme values
extremeFoX = solve(eqDfoX, x)
print(f"The extreme values of the function f(x) = {foX} are at x = {extremeFoX}")
