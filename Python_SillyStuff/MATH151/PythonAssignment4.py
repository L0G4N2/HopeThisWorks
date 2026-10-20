from sympy import *

x = symbols('x')
y = symbols('y')

# Problem 1             P(t) = P_0 * e**kt

k = symbols('k', real = True)
t = symbols('t', real = True)

P_0 = 400
PoT = P_0 * exp(k * t) # type: ignore

# Part A                P(t) = 4000     P_0 = 400       t = 6
subbedPoT = Eq(4000, PoT).subs(t, 6)
solvedPoT = solve(subbedPoT, k)[0].evalf()
print(f"The growth rate of P(t) when 500 bacteria grows to 4000 in 6 hours is: {solvedPoT}")

# Part B                Find the error after 10 hours and test for 6% of the observation
predictPoT = (PoT.subs(t, 10)).subs(k, solvedPoT)
errorPoT = 100 * abs(15200 - predictPoT) / abs(15200)
print(f"The error between the observed number of bacteria, 15200, and the predicted value, {predictPoT}, is off by {errorPoT}% and is not within 6%.")

# Part C                What time will the model predict 50000 bacteria to two decimal places
subbedPoT = Eq(50000, PoT).subs(k, solvedPoT)
# timePoT = solve(subbedPoT, t)[0].evalf()
# print(f"The model predicts that the bacteria will grow to 50000 after {timePoT:.2f} hours.")

# Problem #2            S(r) = (r^3 * sqrt(r + 1)) / (r + 2)^2      r > 0
r = symbols('r', real = True, positive = True)
SoR = ((r**3) * sqrt(r + 1)) / (r + 2)**2

# Part A                S'(r) = ? (factored form)
dSoR = diff(SoR)
factorDSoR = factor(dSoR)
print(f"The factored form of the derviative of S(r) is: {factorDSoR}")

# Part B                Find S(2), S'(2), S'(2) / S(2), and the performance index
SoRTwo = SoR.subs(r, 2)
dSoRTwo = dSoR.subs(r, 2)
relRateSoRTwo = dSoRTwo / SoRTwo
print(relRateSoRTwo)

# Part C                On 1 <= r <= 5, find where S'(2) / S(2) = 5
relRateFive = Eq(5, relRateSoRTwo)
solvedRelRateInterval = solveset(relRateSoRTwo, r, domain=Interval(1, 5))
print(solvedRelRateInterval)
# plot(SoR, dSoR, (r, 1, 5), legend=True, title="S(r), S'(r)")

# Problem 3             C(t) = 20 + Ae^(-kt) in ppm and t is minutes. C(0) = 120    C(5) = 42
A = 100
CoT = 20 + A * exp(-k * t) # type: ignore

# Part A                Find k to three decimals
equalCoT42 = Eq(42, CoT).subs(t, 5)
solvedK = solve(equalCoT42, k)[0].evalf()
print(f"The value of k when C(5) = 42 is: {solvedK:.3f}")

# Part B                Find C'(5), include units, and the sign. C(8) = 29.5    Determine if the model is within 1ppm
dCoT = diff(CoT, t)
dCoTEight = (dCoT.subs(t, 8)).subs(k, solvedK)
print(f"The model predicts that there will be {dCoTEight:.3f} ppm at 8 minutes. Is it within 1 ppm? {abs(29.5 - dCoTEight) <= 1}") # type: ignore

# Part C                C(t) is safe <= 25. Find and report to two decimals, then plot over 0 <= t <= 15
equalCoT25 = Eq(25, CoT).subs(k, solvedK)
# solvedT = solve(equalCoT25, t)
# print(solvedT)
# plot(CoT, solvedT, (t, 0, 25), legend=True, title="C(t) and C(t) = 25")