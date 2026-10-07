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
print(f"The value of f'({a}) is equal to: {dFoX.subs(x, a)}")

# Part B

