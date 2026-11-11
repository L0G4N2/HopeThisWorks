from sympy import *

x = symbols('x', real=True)
y = symbols('y', real=True)

# Problem 1         h(x) = 5 + (5 - x)sin(x) where 0 <= x <= 10
hoX = 5 + (5 - x) * sin(x)

# Part A            Find coordinates of the endpoints and write an equation L(x) then plot
firstEndPoint = hoX.subs(x, 0)
secondEndPoint = hoX.subs(x, 10)

slope = (secondEndPoint - firstEndPoint) / (10 - 0)
loX = firstEndPoint + x * slope

plot(hoX, loX, (x, 0, 10), legend=True, title='h(x) and L(x)')

# Part B            Verify that h statisfies the hypothesis of Mean Value Theorem on [0, 10]. Estimate points that satisfy the conclusion
print("The function h(x) is continuous on every point on the interval [0, 10] because it is composed of polynomial and trionometric functions that are continuous everywhere.")
print("For that same reason, this also makes h(x) differentiable at every point on this interval.")
print("The Mean Value Theorem concludes that there exists at least one number, c, in (0, 10) such that the instantaneous rate of change (derivative) at c equals the average rate of change across the whole interval:")
print(f"h'(c) = (h(10) - h(0))/(10 - 0) = {slope} = slope")
print("As visualized on the graph of h(x) and L(x), at every one of the local extrema (4 locals), the slope of the graph matches the slope of the cable very briefly, thus satisfying the conclusion.")

# Part C            Find every point in (0, 10) where the tangent line is parallel to the cable. Round to 3 decimals and compare to Part B
dHoX = diff(hoX)
guesses = [1, 4, 6, 8] # These points are closest to the extrema
cHoX = list(set([nsolve(Eq(slope, dHoX), x, guess) for guess in guesses]))
cHoX.sort()
print(f"The c values at which the tangent line to the graph equals the slope of the cable are: {cHoX[0]:.3f}, {cHoX[1]:.3f}, {cHoX[2]:.3f}, {cHoX[3]:.3f}")
print("Four values were predicted in Part B due to there existing four local extrema on the interval [0, 10] and four c values were found on this interval which matches the expectation.")

# Problem 2         


# Problem 3         y = 12 - (x^2) / 3 ; -6 <= x <= 6
y = 12 - ((x**2) / 3)

# Part A            Plot the graph and a display at x = 3, as well as the width, height, and area A(x), then state domain of A(x)
# area = height * width
width = 2 * x; height = y
aoX = width * height
plot(y, (x, -6, 6), rectangles=[{"xy":(-3, 0), "width": 6, "height": 9, "color": "orange"}])
print("The domain of this function needs to have a value greater than 0 for the height and a value less than 6 for the width. Therefore, the domain is: 0 < x < 6")

# Part B            Find the dimensions that maximize the area of the rectange, return exact values
dAoX = diff(aoX)
guesses = [0, 1, 2, 3, 4, 5, 6]
solvedAoX = list(set([nsolve(Eq(dAoX, 0), x, guess) for guess in guesses]))
solvedAoX.sort()
