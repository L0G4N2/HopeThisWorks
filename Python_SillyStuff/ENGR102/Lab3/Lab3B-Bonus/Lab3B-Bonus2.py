# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-Bonus2
# Date:         8 September 2026

from math import *

# Function 1: f(x) = sin(x) / x
print("These values will be printed without formatting.")
i = 0
while i != -8:
    temp = sin(pow(10, i)) / pow(10, i)
    print(f"sin({pow(10, i)}) / {pow(10, i)} = {temp}")
    i -= 1
print("----------------------------------------")

# Repeat with values rounded to 8 digits
print("These next values are printed to 8 decimal place format.")
i = 0
while i != -8:
    temp = sin(pow(10, i)) / pow(10, i)
    print(f"sin({pow(10, i)}) / {pow(10, i)} = {temp:.8f}")
    i -= 1
print("----------------------------------------")
