# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Bonus
# Date:         3 September 2026

import math as m

functions = ["sin(x) / x", "(1 - cos(x)) / x^2", "(1 + 1/x)^x"]

# Function 1: f(x) = sin(x) / x
print(f"Function 1: My guess is that {functions[0]} will approach 1")
i = 0
while i != -8:
    temp = m.sin(m.pow(10, i)) / m.pow(10, i)
    print(f"sin({m.pow(10, i)}) / {m.pow(10, i)} = {temp}")
    i -= 1
print("----------------------------------------")
# The limit of f(x) as x approaches 0 appears to approach 1

# Function 2: g(x) = (1 - cos(x)) / x^2
print(f"Function 2: My guess is that {functions[1]} will approach 0")
i = 0
while i != -8:
    # Instead of squaring x, I divided by x again because squaring x has a rounding error which returns an incorrect value
    # So, I am using ([1 - cos(x)] / x) / x instead of (1 - cos(x)) / x^2, which returns the correct value
    temp = ((1 - (m.cos(m.pow(10, i)))) / m.pow(10, i)) / m.pow(10, i)
    print(f"(1-cos({m.pow(10, i)})) / ({(m.pow(10, i))})^2 = {temp}")
    i -= 1
print("----------------------------------------")
# The limit of g(x) as x approaches 0 appears to approach 0.5

# Function 3: h(x) = (1 + 1/x)^x
print(f"Function 3: My guess is that {functions[2]} will approach 2")
i = 0
while i != 8:
    temp = m.pow((1 + (1 / m.pow(10, i))), m.pow(10, i))
    print(f"(1 + 1/{m.pow(10, i)})^{m.pow(10, i)} = {temp}")
    i += 1
print("----------------------------------------")
# The limit of h(x) as x approaches infinity appears to approach 2.718, or e
