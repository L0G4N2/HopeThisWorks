# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-1A
# Date:         8 September 2026

from math import *

# Kinetic Energy = 0.5(mass)(velocity)^2
mass = float(input("Enter the mass of the object in kilograms: "))
velocity = float(input("Enter the velocity of the object in meters per second per second: "))

# Solve for the kinetic energy of the object
kineticEnergy = 0.5 * mass * pow(velocity, 2)

# Print the result of the equation
print(f"The kinetic energy for a object of mass {mass}kg moving at {velocity}m/s/s is: {kineticEnergy}J.")
