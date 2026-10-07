# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab1B-1
# Date:         27 August 2026

import math

# Name, student ID, and section number
print("Name: Logan Gutierrez  UIN: 737008832  Section #: 555\n")

# Interesting fact about myself
print("An interesting fact about myself is that my family has lived in Texas since before Texas was annexed to the United States of America!\n")

# A calculation using Ohms Law
# Ohms Law: V = IR where V is voltage, I is the current, and R is the resistance
voltage = 20 * 5
print(f"The voltage across a conductor with resistance 20(ohms) and a current of 5(Amps) is: {voltage}V\n")

# A calculation of kinetic energy in Joules of an object with mass 100(kg) and velocity 21(m/s)
# Kinematic Energy = 0.5(mass)(velocity)^2 where mass is in kilograms and velocity is in meters per second
kineticEnergy = 0.5 * 100 * math.pow(21, 2)
print(f"The kinetic energy of an object with mass 100(kg) and velocity 21(m/s) is: {kineticEnergy}J\n")

# A calculation of the Reynolds Number for a fluid with velocity 100(m/s) and kinematic viscosity 1.22(m^2/s) with characteristic linear dimension 2.5(m)
# Reynolds Number: (uL)/v where u is the flow velocity in meters per second, L is the characteristic length in meters, and v is the kinematic viscosity in meters squared per second
reynoldsNumber = (100 * 2.5) / 1.22
print(f"The Reynolds Number for a fluid with velocity 100(m/s) and kinematic viscosity 1.22(m^2/s) with a characteristic linear dimension 2.5(m) is: {reynoldsNumber}\n")
