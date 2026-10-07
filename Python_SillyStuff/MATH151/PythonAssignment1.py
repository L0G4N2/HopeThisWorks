import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')

# Question #1:

# 1A. [(4e-4.5)^3.2 + 12^2] / [6 * [ln(3.4)]^2 - 5 * 8]
numerator =  float(((4 * sp.E) - 4.5)**3.2 + 12**2)
denominator = 6 * (sp.ln(3.4))**2 - (5 * 8)
print(f"The result of 1.A. is: {numerator / denominator:.8f}")

# 1.B. sin([5 * PI] / 7) * arctan(15) - sec([2 * PI] / 5)
sine = sp.sin((5 * sp.pi) / 7)
arcTan = sp.atan(15)
secant = sp.sec((2 * sp.pi) / 5)
print(sp.simplify(sine * arcTan - secant))
print(f"The result of 1.B. is: {sine * arcTan - secant:.8f}")

# Question #2:
functionF = sp.tan(2 * x) / (3 * x)

# 2.A. Values of: f(0.01), f(0.0001), and f(0.000001)
first = (functionF.subs(x, 0.01))
second = (functionF.subs(x, 0.0001))
third = (functionF.subs(x, 0.000001))
print(f"The values of f(0.01), f(0.0001), and f(0.000001) are: {first:.8f}, {second:.8f}, and {third:.8f}, respectively")

# 2.B. Values of: f(-0.01), f(-0.0001), and f(-0.000001)
first = (functionF.subs(x, -0.01))
second = (functionF.subs(x, -0.0001))
third = (functionF.subs(x, -0.000001))
print(f"The values of f(-0.01), f(-0.0001), and f(-0.000001) are: {first:.8f}, {second:.8f}, and {third:.8f}, respectively")

# 2.C. Limit of f(x) as x approaches 0
functionF = (sp.tan(2 * x)) / (3 * x)
limit = sp.limit(functionF, x, 0)
print(f"The limit of f(x) as x approaches 0 is: {limit}")

# Question #3:      p(t) = (200t + 350) / (0.8t + 7)
t = sp.symbols('t')
functionP = (200 * t + 350) / (0.8 * t + 7)

# 3.A.  Deer in the forest after 5 years?
print(f"There would be {functionP.subs(t, 5).round()} deer in the forest after 5 years.")

# 3.B.  How many years have past when there are 200 deer?
yVal = 200
equation = sp.Eq(y, functionP)
solvedP = equation.subs(y, yVal)
solutionP = sp.solve(solvedP, t)
print(f"There will be 200 deer in the part after {solutionP[0]:.2f} years.")

# 3.C.  The maximum number of deer in the park? (Limit as x approaches infinity)
limit = sp.limit(functionP, t, sp.oo)
print(f"The population of deer in the park will eventually level off at {limit} deer as time progresses.")

# Question #4:
a = sp.symbols('a')
functionF = sp.Piecewise(((280 * x**2) + (a * x) - 40, x < 2), ((a**2) * x, x >= 2))
piecewise1 = (280 * x**2) + (a * x) - 40
piecewise2 = (a**2) * x

# 4.A.  The limit of f(x) as x approaches negative infinity
subFuncF = functionF.subs(a, 1)
limit = sp.limit(piecewise1, x, -sp.oo)
print(f"The limit of f(x) as x approaches infinity is: {limit}")
# Printing how 'a' affects the limit
print("The value of \'a\' will not affect the limit because the function continues forever towards positive infinity.", end=" ")
print("However, the value of \'a\' will affect the rate at which the function f(x) approaches infinity, or how fast f(x) approaches infinity.")

# 4.B.  Using .solve() to solve for what value of 'a' will make f(x) be continuous at x = 2
continuityEq = sp.Eq(piecewise1, piecewise2)
eqSubbed = continuityEq.subs(x, 2)
solvedVals = sp.solve(eqSubbed, a)
print(f"The values of \'a\' that make f(x) continuous at x=2 are: ", end="")
for i in range(len(solvedVals)):
    print(solvedVals[i].evalf(), end=", ")
