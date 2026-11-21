import sympy as sp, matplotlib.pyplot as plt

x = sp.symbols('x')

# Problem 1         f(x) = 2 - |x - 3|      0 <= x <= 6
foX = 2 - abs(x - 3)

# Part A            Plot f(x) and identify x-intercepts and sign of f(x)
sp.plot(foX, (x, 0, 6))    # f(x) is positive from (1, 5) and negative outside of that interval

# Part B            Find integral of f(x) and |f(x)| from 0 to 6
intFoX = sp.integrate(foX, (x, 0, 6))
absIntFoX = sp.integrate(abs(foX), (x, 0, 6))

print(f"The definite integral of f(x) from 0 to 6 is: {intFoX}")
print(f"The definite integral of |f(x)| from 0 to 6 is: {absIntFoX}")

# Part C            Create a scatterplot of the midpoint estimates for 1 <= n <= 12
n = 1; MnTable = []; MnErrorTable = []
while n <= 12:
    Mn = 0; deltaX = 6 / n
    for i in range(1, n + 1):
        Mn += foX.subs(x, deltaX * (i - 0.5))
    Mn *= deltaX
    MnTable.append(Mn)
    MnErrorTable.append(abs(Mn - intFoX)) # type: ignore
    print(f"n = {n:2d} | M_n = {Mn:.4f} | Error = {abs(Mn - intFoX):.4f}") # type: ignore
    n += 1

xVal = list(range(1, n))
yVal = MnErrorTable
plt.scatter(xVal, yVal)
plt.xlabel("n, the number of subintervals"); plt.ylabel("|Mn - integral{f(x) dx}(0, 6)|")
plt.show()

# Problem 2         f(t) = 3(t - 1)(t - 3), A(x) = integral{f(t) dt}(0, x)      0 <= t <= 4
t = sp.symbols('t')
foT = 3 * (t - 1) * (t - 3)
aoX = sp.integrate(foT, (t, 0, x))

# Part A            Find A(x), factor, and verify A(0) = 0 and A'(x) = f(x), then plot(f(x), A(x), (x, 0, 4))
foX = foT.subs(t, x)
sp.plot(foX, aoX, (x, 0, 4))

# Part B            Use Fundamental Theorem of Calculus to determine when A(x) is increasing and decreasing, then find greatest and least values
dAoX = sp.diff(aoX)
critNums = sp.solve(sp.Eq(0, dAoX), x)

# Values to test if A(x) increasing or decreasing
testVals = [0, 1, 2, 3, 4]
values = [foX.subs(x, val) for val in testVals]
breakpoints = [0] + sorted(critNums) + [4]

for left, right in zip(breakpoints, breakpoints[1:]):
    midpoint = (left + right) / 2
    if dAoX.subs(x, midpoint) > 0: # type: ignore
        print(f"A(x) is increasing on ({left}, {right})")
    else:
        print(f"A(x) is decreasing on ({left}, {right})")

# Part C            B(x) = integral{f(t) dt}(x, x + 1)      0 <= x <= 3, find and simplify B(x)

# Integrate f(t) from x to x + 1 and simplify
boX = sp.simplify(sp.integrate(foT, (t, x, x + 1)))
print("B(x) =", boX)

# Verify B'(x) = f(x + 1) - f(x)
dBoX = sp.diff(boX, x)
ftcRHS = sp.simplify(foX.subs(x, x + 1) - foX)
print(f"B'(x) = {dBoX}")
print(f"f(x + 1) - f(x) = {ftcRHS}")
print(f"Does B'(x) == f(x + 1) - f(x)? {sp.simplify(dBoX - ftcRHS) == 0}")

# Plot B(x) on [0, 3]
sp.plot(boX, (x, 0, 3))

# Find greatest and least values of B(x) on [0, 3]
critNums = sp.solve(dBoX, x)
testPoints = [0, 3] + [c for c in critNums if 0 <= c <= 3]
bVals = {point: boX.subs(x, point) for point in sorted(set(testPoints))}
print(f"Values of B(x) at candidates (x: B(x)): {bVals}")
print(f"Greatest value: {max(bVals.values())} at x = {[k for k, v in bVals.items() if v == max(bVals.values())]}")
print(f"Least value: {min(bVals.values())} at x = {[k for k, v in bVals.items() if v == min(bVals.values())]}")

# Problem 3         P(t) = 6sin(PI*t / 6)           0 <= t <= 12
poT = 6 * sp.sin((sp.pi * t / 6)) # type: ignore

# Part A            Find general antiderivative of P(t) then find energy store in battery when E(0) = 50 and E'(t) = P(t)
C = sp.symbols('C')
eoTGen = sp.integrate(poT) + C
eoT0 = sp.solve(sp.Eq(eoTGen.subs(t, 0), 50), C)[0].evalf()
eoT = eoTGen.subs(C, eoT0)
sp.plot(poT, eoT, (t, 0, 12))

# Part B            Find the change in stored energy from 0 <= t <= 6 and 0 <= t <= 12
deltaE6 = eoT.subs(t, 6) - eoT.subs(t, 0)
deltaE12 = eoT.subs(t, 12) - eoT.subs(t, 0)
greatest = 0; least = eoT.subs(t, 12); vals = [0, 6, 12]
for val in vals:
    greatest = eoT.subs(t, val) if eoT.subs(t, val) > greatest else greatest
    least = eoT.subs(t, val) if eoT.subs(t, val) < least else least
print(f"Greatest amount of stored energy: {greatest.evalf():.3f} at {sp.solve(sp.Eq(greatest, eoT), t)}") # type: ignore
print(f"Least amount of stored energy: {least.evalf():.3f} at {sp.solve(sp.Eq(least, eoT), t)}")
