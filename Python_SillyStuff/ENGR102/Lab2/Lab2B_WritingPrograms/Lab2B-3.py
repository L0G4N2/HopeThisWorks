# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Logan Gutierrez 737008832
# Section:      555
# Assignment:   2B-3
# Date:         1 September 2026

# Only these lines of code can be used to complete the program. You may not add any additional lines of code.
#   x = 1
#   y = 10
#   z = 0
#   x = y
#   x += 1
#   y += x
#   y *= x
#   z += x
#   z += y
#   print(z)

# Print 1:
x = 1
y = 10
z = 0

z += x
print(z)
# Final Values: x = 1, y = 10, z = 1

# Print 3:
z += x
z += x
print(z)
# Final Values: x = 1, y = 10, z = 3

# Print 11:
z = 0
y += x
z += y
print(z)
# Final Values: x = 1, y = 11, z = 11

# Print 28:
z += y
x += 1
x += 1
z += x
z += x
print(z)
# Final Values: x = 3, y = 11, z = 28

# Print 123:
x = y
y *= x
x = 1
z = 0
z += y
z += x
z += x
print(z)
# Final Values: x = 3, y = 33, z = 123

# Print 10^32:
z = 0
x = 1
y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z += y
print(z)
# Final Values: x = 10^16, y = 10^32, z = 10^32

# Print 4321:
x = 1
y = 10
z = 0
x += 1
y += x
x = y
y *= x
x = 1
x += 1
x += 1
y *= x
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
x = 1
y += x
z += y
print(z)
# Final Values: x = 10, y = 4320, z = 4321
