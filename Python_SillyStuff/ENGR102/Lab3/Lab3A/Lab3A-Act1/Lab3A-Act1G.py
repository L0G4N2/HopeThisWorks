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

import math as m

# Voltage to voltage level(dbV): V = 10^(dbV / 20) -> dbV = 20log_10(V)
voltage = float(input("Enter the number of voltage to convert to decibal volts: "))
dbV = 20 * m.log10(voltage)
print(f"{voltage}V is equal to {dbV}dbV.")
