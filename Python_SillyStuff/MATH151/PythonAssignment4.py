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
