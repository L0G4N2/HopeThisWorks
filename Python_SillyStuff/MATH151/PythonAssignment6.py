from sympy import *

x = symbols('x')
y = symbols('y')

# Problem 1         h(x) = 5 + (5 - x)sin(x) where 0 <= x <= 10
hoX = 5 + (5 - x) * sin(x)

# Part A            Find coordinates of the endpoints and write an equation L(x) then plot
firstEndPoint = hoX.subs(x, 0)
secondEndPoint = hoX.subs(x, 10)

loX = firstEndPoint + x * (secondEndPoint - firstEndPoint) / (10 - 0)

plot(hoX, loX, (x, 0, 10), legend=True, title='h(x) and L(x)')

# Part B            Verify that h statisfies the hypothesis of Mean Value Theorem on [0, 10]. Estimate points that satisfy the conclusion


# Part C            Find every point in (0, 10) where the tangent line is parallel to the cable. Round to 3 decimals and compare to Part B
