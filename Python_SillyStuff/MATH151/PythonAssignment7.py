from sympy import *

x = symbols("x")

# Energy_water = 1.4 * Energy_Land
# c = sqrt(a^2+b^2)

# calculate water and land distance
water_distance = sqrt(5**2 + x ** 2)
land_distance = 13 - x

# make energy equation
E_x = (1.4 * water_distance) + land_distance # type: ignore
print(E_x)

# plot energy equation
plot(E_x, (x, 0, 13), title = "Energy of Bird" )

# approximate best landing point
print("The best landing point is approximately at 18 units at x = 5.5")

# Find the approximate value of x that takes the least energy
E_prime_x = diff(E_x, x)
crit_nums = solve(E_prime_x, x)
print(f"The approximate x value that takes the least energy is {crit_nums[0]:.3f}")

# Calculate the exact x value
E_exact = Rational(7,5) * water_distance + land_distance # type: ignore
crit_exact = solve(diff(E_exact, x), x)
print(f"The exact x value that takes the least energy is {crit_exact[0]}")

# Calculate the number of kilometers the bird flies
distance_water = water_distance.subs(x, crit_exact[0])
distance_land = land_distance.subs(x, crit_exact[0])
print(f"The bird flies {distance_water.evalf():.3f} km over water.") # type: ignore
print(f"The bird flies {distance_land.evalf():.3f} km over land.")
print(f"The total distance is {(distance_water + distance_land).evalf():.3f} km")

# repeat with the water constant
water_constant = [1.00, 1.05, 1.10, 1.20, 1.40, 1.80]

for i in water_constant:
    water_distance = sqrt(5**2 + x ** 2)
    land_distance = 13 - x
    E_x = (i * water_distance) + land_distance # type: ignore
    print(E_x)
    plot(E_x, (x, 0, 13), title = "Energy of Bird" )

# Problem 2         a(t) = 6t - 15      0 <= t <= 5     p(0) = 5; v(0) = 18
t = symbols('t')
aoT = 6 * t - 15

# Part A            Find the vertical velocity and height of the drone
voT = integrate(aoT) + 18 # type: ignore
hoT = integrate(voT) + 5 # type: ignore

print(f"The equations for the vertical velocity is represented by: v(t) = {voT}")
print(f"The equations for the vertical height is represented by: h(t) = {hoT}")

# Part B            Find every time for when the drone changes direction and find its height at these times. Plot from 0 <= t <= 5
critNums = solve(Eq(voT, 0), t)
heights = [hoT.subs(t, num) for num in critNums]
plot(hoT, (t, 0, 5))

# Part C            Find the time of drones change in height, greatest height, and lowest height
hoT0 = hoT.subs(t, 0); hoT5 = hoT.subs(t, 5)
deltaHoT = (hoT5 - hoT0).evalf()

max = hoT5; min = hoT0
for height in heights:
    if height > max:
        max = height
    if min > height:
        min = height
print(f"Change in height: {deltaHoT} ft| Max (time (s), height (ft)): {solve(Eq(hoT, max), t)[0].evalf(), max} | Min (time (s), height (ft)): {solve(Eq(hoT, min), t)[0].evalf(), min}")

# Problem 3         v(t) = 90e^(-t/4)   0 <= t <= 12
voT = 90 * exp(-t / 4) # type: ignore
doT = integrate(voT)

# Part A            Divide interval into n equal parts (DELTA_T = 12 / n) where n = 6, then find L_6 and R_6 and plot a rectangle
n = symbols('n')
deltaT = (12 / n).subs(n, 6)

L_n = 0
for i in range(0, 6):
    L_n += voT.subs(t, i * deltaT) * deltaT
R_n = 0
for i in range(1, 7):
    R_n += voT.subs(t, i * deltaT) * deltaT

L_n = L_n.evalf(); R_n = R_n.evalf() # type: ignore

leftRects = []
for i in range(0, 6):
    leftX = i * deltaT
    rightX = (i + 1) * deltaT
    height = voT.subs(t, leftX)
    leftRects.append({"xy": (leftX, 0), "width": deltaT, "height": height, "alpha": 0.4})
plot(voT, (t, 0, 12), rectangles=leftRects)

rightRects = []
for i in range(1, 7):
    rightX = i * deltaT
    leftX = rightX - deltaT
    height = voT.subs(t, rightX)
    rightRects.append({"xy": (leftX, 0), "width": deltaT, "height": height, "alpha": 0.4})
plot(voT, (t, 0, 12), rectangles=rightRects)

# Part B            Find L_n and R_n for n = 12, 24, 48, 96. Give estimates and their differences
ns = [12, 24, 48, 96]
for val in ns:
        
    # Left-endpoint sum
    L_n = 0
    for i in range(0, val):
        L_n += voT.subs(t, i * deltaT) * deltaT
        
    # Right-endpoint sum
    R_n = 0
    for i in range(1, val):
        R_n += voT.subs(t, i * deltaT) * deltaT
        
    difference = L_n - R_n
    print("n =", val, "| L_n =", L_n.evalf(), "| R_n =", R_n.evalf(), "| Difference =", difference.evalf()) # type: ignore

# Part C            Find the antiderivative V(t) for v(t) then use V(12) - V(0) to find the actual distance traveled and find the error in each
actual = (doT.subs(t, 12) - doT.subs(t, 0)).evalf()
print(f"Antiderivative: {doT}")
print(f"Actual Difference: {actual}")

for val in ns:
        
    # Left-endpoint sum
    L_n = 0
    for i in range(0, val):
        L_n += voT.subs(t, i * deltaT) * deltaT
        
    # Right-endpoint sum
    R_n = 0
    for i in range(1, val):
        R_n += voT.subs(t, i * deltaT) * deltaT
        
    leftError = abs(L_n.evalf() - actual) # type: ignore
    rightError = abs(R_n.evalf() - actual) # type: ignore
    print("n =", val, "| Left Error =", leftError, "| Right Error =", rightError) # type: ignore

n = 1
while True:
    deltaT = 12 / n
    ratio = exp(-deltaT / 4)
    L_n = (90 * deltaT * (1 - exp(-3)) / (1 - ratio)).evalf() # type: ignore    
    R_n = (L_n * ratio).evalf()
    if abs(L_n - actual) < 1 and abs(R_n - actual) < 1:
        print(f"First value of n to have both errors be less than 1 foot: {n}")
        break
    n += 1
