from sympy import *

# Problem 1     f(x) = (x^2 + x - 6) / (x - 2)  x != 2

x = symbols('x')
foX = ((x ** 2) + x - 6) / (x - 2)

# Part A: Use .subs() to evaluate f(x) at the following values:
numList = [1.9, 1.99, 1.999, 2.001, 2.01, 2.1]
solutions = [foX.subs(x, val) for val in numList]
print(f"The values of f(x) to be evaluated are: {numList}")
print(f"The values of f(x) at the following points are, {solutions}, respectively.")

# Part B: Plot f on 0 <= x <= 4, then predict the limit of f(x) as x approaches 2:
# plot(foX, (x, 0, 4))

# Part C: Use limit() to compute the limit exactly
print(f"The limit of f(x) as x approaches 2 is: {limit(foX, x, 2)}")

# Problem 2     s(t) = t^3 - 6t^2 + 15t

t = symbols('t')
soT = (t**3) - (6 * t**2) + (15 * t)

# Part A: Create the symbolic difference quotient --> q(h) = (s(2 + h) - s(2)) / h, then use simplify() to rewrite q(h)
h = symbols('h')
qoH = (soT.subs(t, 2 + h) - soT.subs(t, 2)) / h

print(f"The simplified form of the symbolic difference is: {qoH.simplify()}")

# Part B: Use .subs() to evaluate q(h) at the following values:
numList = [1, 0.1, 0.01, 0.001]
qHValues = [qoH.subs(h, val) for val in numList]
print(f"The values of f(x) to be evaluated are: {numList}")
print(f"The values of q(h) at the following points are, {qHValues}, respectively.")

# Part C: Use limit() to find lim q(h) as h approaches 0
print(f"The limit of q(h) as h approaches 0 is: {limit(qoH, h, 0)} m/s")

# Part D: Use diff() to define the velocity function v(t) = s'(t), then verify Part C
voT = soT.diff()
print(f"v(2) is equal to: {voT.subs(t, 2)}")
print(f"Is v(2) equal to the limit as q(h) approaches 0? {voT.subs(t, 2) == limit(qoH, h, 0)}")

# Part E: Use solve() to find every t in 0 <= t <= 4 for which v(t) = 6 m/s
y = symbols('y')
eqVoT = Eq(y, voT)
voT6 = eqVoT.subs(y, 6)
solutions = solve(voT6, t)
print(f"v(t) will eqaul 6 m/s when t is equal to the following: {solutions}")

# Problem 3     g(x) = x^3 -4x
goX = (x ** 3) - (4 * x)

# Part A: Use diff() to find g'(x)
dGoX = diff(goX)
print(f"The derviative of g(x) is: {dGoX}")

# Part B: Find the point on the graph and the slope of the graph at x = 2
slope = dGoX.subs(x, 2)
yGoX = goX.subs(x, 2)
print(f"The point on the graph where x = 2 is: (2, {yGoX}), and the slope of the tangent line is: {slope}")

# Part C: Define the tangent line at L(x) = g(2) + g'(2)(x - 2), then use expand() to put L(x) in the form of mx + b
loX = goX.subs(x, 2) + dGoX.subs(x, 2) * x - 2
expandedLoX = loX.expand()
print(f"The expanded form of L(x) is: {expandedLoX}")

# Part D: Plot g(x) and L(x) on the same axis for 0 <= x <= 3
# plot(goX, loX, (x, 0, 3))

# Problem 4     A(r) = pi * r^2     V(r) = 4/3 * pi * r^3

# Part A: Use diff() to compute A'(r) and V'(r)
r = symbols('r')

aoR = pi * (r ** 2)
voR = (4 / 3) * pi * (r ** 3)

dAoR = diff(aoR)
dVoR = diff(voR)

print(f"The derivative of the area of a circle is: {dAoR}, and the derivative of the volume of a sphere is: {dVoR}")

# Part B: Evaluate A'(3) and V'(3) exactly and approximately and explain what the numbers mean in geometric terms
aoR3 = aoR.subs(r, 3).evalf()
voR3 = voR.subs(r, 3).evalf()
print(f"A'(3) is equal to, {aoR3}, and represents the circumference of a circle in meters.")
print(f"V'(3) is equal to, {voR3}, and represents the surface area of a sphere in square meters.")
