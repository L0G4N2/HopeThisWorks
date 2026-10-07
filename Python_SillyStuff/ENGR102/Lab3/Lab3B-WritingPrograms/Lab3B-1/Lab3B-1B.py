# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-1B
# Date:         8 September 2026

import math as m

# Using this function instead of m.radians because m.radians has a round-off error that returns an incorrect value
def toRadians(degrees):
    return degrees * (m.pi / 180)

# Mohr–Coulomb Failure Criterion: shearStrength = stressNormal * tan(theta) + cohesion
normalStress = float(input("Enter the normal stress of the object in kilopascals: "))
theta = float(input(f"Enter the angle of internal friction in degrees from 0 < \u03b8 < 90: "))
cohesion = float(input("Enter the cohesion of the material in kilopascals: "))

# Solve for the shear strength at failure
shearStrength = normalStress * m.tan(toRadians(theta)) + cohesion

# Print the result of the equation and truncate the shear strength at 8 decimal places
print(f"The shear strength of an object with a normal stress of {normalStress}kPa, an angle of internal friction of {theta}\u00b0", end=", ")
print(f"and a cohesion of {cohesion}kPa is: {shearStrength:.8f}kPa.")
