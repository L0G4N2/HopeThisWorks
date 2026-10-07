# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-Bonus1
# Date:         8 September 2026

# Prompt for number of digits
digits = int(input("How many decimal places do you want to output? "))

# Print the decimal of 1/7 and truncate at the number of digits provided by the user
print(f"{1/7:.{digits}f}")
