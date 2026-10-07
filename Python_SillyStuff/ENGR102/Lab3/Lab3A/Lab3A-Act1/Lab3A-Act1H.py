# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Name
#               Name
#               Name
# Section:      555
# Assignment:   Lab3A-Act1A
# Date:         8 September 2026

# Difference between two Richter scale values to the ratio of energy of released in two earthquakes
# The magnitude on the Richter Scale is related to Energy Released by such: log_10(E) = 4.4 + 1.5M
# Where E is the energy released and M is the magnitude
# E = 10^(4.4 + 1.5M)   M = (log_10(E) - 4.4) / 1.5
# Ratios of Energy: E2 / E1 = 10^(M1 - M2) => E2 = (E1)(10^[M1 - M2])
# Ratios of Energy: E2 / E1 = 10^(M1 - M2) => E1 = E2 / (10^[M1 - M2])
richter1 = float(input("Enter the magnitude of the first earthquake on the Richter Scale: "))
energyRel1 = 10**(4.4 + 15 * richter1)
richter2 = float(input("Enter the magnitude of the second earthquake on the Richter Scale: "))
energyRel2 = 10**(4.4 + 15 * richter2)

diffOfScale = richter2 - richter1
ratioE2ToE1 = energyRel1 * (10**(richter1 - richter2))
ratioE1ToE2 = energyRel2 / (10**(richter1 - richter2))

# Print Energies
print(f"Energy 1: {energyRel1}\nEnergy 2: {energyRel2}")

# Print Ratios
print(f"The difference in magnitudes of the earthquakes are: {diffOfScale}")
print(f"The ratio of energy released of the second earthquake to the first is: {ratioE2ToE1}")
print(f"The ratio of energy released of the first earthquake to the second is: {ratioE1ToE2}")
