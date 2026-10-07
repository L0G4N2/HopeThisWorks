# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Logan Gutierrez 737008832
# Section:      555
# Assignment:   2B-1
# Date:         1 September 2026

import math

# Name, student ID, and section number
print("Name: Logan Gutierrez  UIN: 737008832  Section #: 555\n")

# Interesting fact about myself
print("An interesting fact about myself is that my family has lived in Texas since before Texas was annexed to the United States of America!\n")

# A calculation using Ohms Law
# Ohms Law: V = IR where V is voltage, I is the current, and R is the resistance
current = 5
resistance = 20
voltage = resistance * current
print(f"The voltage for a current of {current}(amps) going through a {resistance}(ohm) resistor is: {voltage}V\n")

# A calculation of kinetic energy in Joules of an object with mass 100(kg) and velocity 21(m/s)
# Kinematic Energy = 0.5(mass)(velocity)^2 where mass is in kilograms and velocity is in meters per second
mass = 100
velocity = 21
kineticEnergy = 0.5 * mass * math.pow(velocity, 2)
print(f"The kinetic energy of an object with mass {mass}(kg) and velocity {velocity}(m/s) is: {kineticEnergy}J\n")

# A calculation of the Reynolds Number for a fluid with velocity 100(m/s) and kinematic viscosity 1.2(m^2/s) with characteristic linear dimension 2.5(m)
# Reynolds Number: (uL)/v where u is the flow velocity in meters per second, L is the characteristic length in meters, and v is the kinematic viscosity in meters squared per second
flowVelocity = 100
characteristicLength = 2.5
kinematicViscosity = 1.2
reynoldsNumber = (flowVelocity * characteristicLength) / kinematicViscosity
print(f"The Reynolds Number for a fluid with velocity {flowVelocity}(m/s) and kinematic viscosity {kinematicViscosity}(m^2/s) with a characteristic linear dimension {characteristicLength}(m) is: {reynoldsNumber}\n")
