from sympy import *

x = symbols('x')
y = symbols('y')

# Problem #1    f(x) = (3x^2 - 5x + 2) * sin(x)

foX = (3*x**2 - 5*x + 2) * sin(x)

# Part A        Find f'(x) and f''(x)
foXPrime = foX.diff()
foXDoublePrime = foXPrime.diff()
print(f"f'(x) = {foXPrime}")
print(f"f''(x) = {foXDoublePrime}")

# Part B        Plot f(x), f'(x), and f''(x) on the same axes from 0 <= x <= 2pi
# plot(foX, foXPrime, foXDoublePrime, (x, 0, 2*pi), legend=True, title="f(x), f'(x), and f''(x) from 0 to 2pi", xlabel="x", ylabel="y")

# Part C        Solve for f'(x) = 0 and plot every x-value where f(x) has a horizontal tangent line


# Problem #2    T(x) = 200 + 10x      THETA(x) = (pi / 6) + (x / 20)      F(x) = T(x)cos(THETA(x))
toX = 200 + 10*x
thetaX = (pi / 6) + (x / 20)
forceX = toX * cos(thetaX)

# Part A        Find F'(x) and include units
forcePrime = forceX.diff()
print(f"F'(x) = {forcePrime} N")

# Part B        Evaluate F(0), F(10), and F'(2) and include units
print(f"F(0) = {forceX.subs(x, 0):.3f} N")
print(f"F(10) = {forceX.subs(x, 10):.3f} N")
print(f"F'(2) = {forcePrime.subs(x, 2):.3f} N")

# Part C        Plot F(x) over 0 <= x <= 10 and find where F'(x) = 0
# plot(forceX, (x, 0, 10), legend=True, title="F(x) over 0 to 10", xlabel="x", ylabel="F(x)")
# print(f"The value of x where F'(x) = 0 is: {solve(Eq(forcePrime, 0), x)}")

# Part D        Report the horizontal force at the value of x where F'(x) = 0
# xValue = solve(Eq(forcePrime, 0), x)[0]
# print(f"The horizontal force at x = {xValue:.3f} is: {forceX.subs(x, xValue):.3f} N")

# Problem #3    x^2 + xy + y^2 = 7
eqFoX = Eq(x**2 + x*y + y**2, 7)

# Part A        Use implicit differentiation to find dy/dx
dyDx = -(diff(eqFoX.lhs, x) / diff(eqFoX.lhs, y)) + diff(eqFoX.rhs, x) / diff(eqFoX.lhs, y)
print(f"dy/dx = {dyDx}")

# Part B        Find the slope and the tangent line at the point (1, 2)
slope = dyDx.subs([(x, 1), (y, 2)])
print(f"The slope of the tangent line at (1, 2) is: {slope}")
tangentLine = slope * (x - 1) + 2
print(f"The equation of the tangent line at (1, 2) is: y = {tangentLine}")

# Part C        Find every point on the graph where the tangent line is horizontal
horizontalTangents = solve(Eq(dyDx, 0), y)
print(f"The points on the graph where the tangent line is horizontal are: {horizontalTangents}")
