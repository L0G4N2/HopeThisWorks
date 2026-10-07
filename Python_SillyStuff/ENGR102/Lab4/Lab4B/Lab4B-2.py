# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab4B-1
# Date:         15 September 2026

from math import *

# Quadratic Formula: x = (-b +- sqrt(b^2 - 4ac)) / 2a
a = float(input("Enter the coefficeint of \'A\' as a real number: "))
b = float(input("Enter the coefficeint of \'B\' as a real number: "))
c = float(input("Enter the coefficeint of \'C\' as a real number: "))

isImaginary = (pow(b, 2)) < (4 * a * c)

# Roots when 'a' does not equal 0
def aNotZero():
    if isImaginary == False:
        posRoot = f"{(-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a):.8f}"
        negRoot = f"{(-b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a):.8f}"
    elif isImaginary:
        posRoot = f"{-b / (2 * a)} + {(sqrt(abs(pow(b, 2) - 4 * a * c))) / (2 * a):.8f}i"
        negRoot = f"{-b / (2 * a)} - {(sqrt(abs(pow(b, 2) - 4 * a * c))) / (2 * a):.8f}i"
    if posRoot == negRoot:
        print(f"The only root of the function, {a}x^2 + {b}x + {c}, is: x={posRoot}")
    else:
        print(f"The roots of the function, {a}x^2 + {b}x + {c}, are: x={posRoot}, {negRoot}")

if a != 0:
    aNotZero()
elif b != 0:
    root = -c / b
    print(f"The only root for the function, {a}x^2 + {b}x + c, is: {root}")
elif c != 0:
    print(f"The provided values create a horizontal line at y={c} and has no roots.")
else:
    print(f"The provided values create a horizontal line at y={c} and has infinite many roots.")
