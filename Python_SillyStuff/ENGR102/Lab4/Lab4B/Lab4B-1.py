# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab4B-1
# Date:         15 September 2026

print("This program compares 3 integer numbers and prints the largest to the console.")
num1 = float(input(f"Enter any real number value #1: "))
num2 = float(input(f"Enter any real number value #2: "))
num3 = float(input(f"Enter any real number value #3: "))

greatest = 0

if num1 > num2 and num1 > num3:
    greatest = num1
    print(f"The greatest of the three numbers is: {greatest}")
elif num2 > num1 and num2 > num3:
    greatest = num2
    print(f"The greatest of the three numbers is: {greatest}")
elif num3 > num1 and num3 > num2:
    greatest = num3
    print(f"The greatest of the three numbers is: {greatest}")
elif num1 == num2 or num1 == 3:
    greatest = num1
    print(f"Two or more of the numbers were equal with {greatest} being the greatest value.")
elif num2 == 1 or num2 == 3:
    greatest = num2
    print(f"Two or more of the numbers were equal with {greatest} being the greatest value.")
