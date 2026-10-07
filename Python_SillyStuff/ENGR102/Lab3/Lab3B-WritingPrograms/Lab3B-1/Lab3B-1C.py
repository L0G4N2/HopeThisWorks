# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-1C
# Date:         8 September 2026

# The Arps Equation: q(t) = q0 / (1 + DBt)^(1/B)
# Where q(t) is the production rate at time = t, q0 is the initial prodution rate, D is the nominal decline rate, and t is time
# B is the decline exponent (B = 0 for exponential, 0 < B < 1 for hyperbolic, and B = 1 for harmonic)
initialProduction = float(input("Enter the initial rate of production in cubic meters per second: "))
nominalDecline = float(input("Enter the nominal decline rate of production in reciprocal seconds: "))
time = float(input("Enter the time of production in seconds: "))
declineExp = float(input("Enter the exponent at which production is declining: "))

# Solve for the production rate at time = t
prodcutionRate = initialProduction / (1 + (nominalDecline * declineExp * time)) ** (1/declineExp)

# Print result of the equation and truncate to 8 decimal places
print(f"The production rate at {time} sesconds, with an initial production rate of {initialProduction} cubic meters per second", end=", ")
print(f"a nominal decline rate of {nominalDecline} reciprocal seconds, and a decline exponent of {declineExp} is: {prodcutionRate} cubic meters per second.")
