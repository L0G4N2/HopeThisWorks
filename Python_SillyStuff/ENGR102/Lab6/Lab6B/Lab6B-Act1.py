# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6B-Act1
# Date:         29 September 2026

# Useful library to perform calculus
from sympy import *

# Variables to be used in functions
x = symbols('x')
y = symbols('y')

def approxDerivative(function, pointA, pointer):
    x1 = 0.1
    iterations = 1
    divisor = 2
    diffAtA = (function.diff()).subs(x, pointA)
    numDiff = (function.subs(x, pointA + x1) - function.subs(x, pointA)) / x1
    difference = abs(abs(numDiff) - abs(diffAtA)).evalf()
    while not(difference <= 1e-8):
        numDiff = ((function.subs(x, pointA + (x1 / divisor)) - function.subs(x, pointA)) / (x1 / divisor)).evalf()
        difference = abs(abs(numDiff) - abs(diffAtA)).evalf()
        divisor *= 2
        iterations += 1
    print(f"After {iterations} iterations, the approximated derivative at {pointer} is: {numDiff}")

# Part A

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

# Differentiate f(x)
dFoX = diff(foX)

# Input a certain x value from the user and compare f(x) to f'(x)
a = float(input("Enter a value of x to solve for the value at f'(x): "))
diffAtA = dFoX.subs(x, a)
print(f"The value of f'({a}) is equal to: {diffAtA}")

# Part B

x1 = 0.1
iterations = 1
divisor = 2
numDiff = (foX.subs(x, a + x1) - foX.subs(x, a)) / x1
difference = abs(abs(numDiff) - abs(diffAtA))
while not(difference <= 1e-6):
    numDiff = (foX.subs(x, a + (x1 / divisor)) - foX.subs(x, a)) / (x1 / divisor)
    difference = abs(abs(numDiff) - abs(diffAtA))
    divisor *= 2
    iterations += 1
print(f"After {iterations} iterations, the approximated value of f'({a}) is, {numDiff}, and is off by the true value by {numDiff - dFoX.subs(x, a)}.")

# Part C

# Approximating the derivative of sin(2x) at x = 2
goX = sin(2 * x)
approxDerivative(goX, 2, "g'(2)")

# Approximating the derivative of ln(1/x) at x = 5
hoX = ln(1 / x)
approxDerivative(hoX, 5, "h'(5)")

# Approximating the derivative of tan(sin(x)) at x = -10
joX = tan(sin(x))
approxDerivative(joX, -10, "j'(-10)")

# Approximating the derivative of e^[cos(x)] at x = 0.3
koX = exp(cos(x))
approxDerivative(koX, 0.3, "k'(0.3)")
