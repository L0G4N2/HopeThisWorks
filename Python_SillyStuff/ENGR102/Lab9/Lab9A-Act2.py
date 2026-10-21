# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab9A-Act2
# Date:         20 October 2026

# Context for the user
print("This program prompts the user to enter two sets of (x, y) coordinates then continuously prompts the user to", end=" ")
print("enter an x-value to calculate linear interpolation or extrapolation depending on where the x-value lies on the interval.", end=" ")
print("The program continues to make these calculations until the user inputs a non-real number.")

# Retrieve coordinates from the user
coords = []
for i in range(2):
    x = float(input(f"Enter x-value #{i + 1} as a real number: "))
    y = float(input(f"Enter y-value #{i + 1} as a real number: "))
    coords.append([x, y])

# Linear Interpolation: y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
def interpolate(x):
    if (x <= coords[1][0] and x >= coords[0][0] and coords[0][0] < coords[1][0]) or (x <= coords[0][0] and x >= coords[1][0] and coords[0][0] > coords[1][0]):
        print(f"Since the x-value, {x}, is between the entered coordinates, the linear interpolation will be: ", end="")
    else:
        print(f"Since the x-value, {x}, is outside of the entered coordinates, the linear extrapolation will be: ", end="")
    return coords[0][1] + ((x - coords[0][0]) * (coords[1][1] - coords[0][1])) / (coords[1][0] - coords[0][0])

# Prompt the user to enter a value of x to interpolate/extrapolate at until they enter an invalid input to end the loop
while True:
    temp = float(input("Enter a real number as an x-value to interpolate/extrapolate on the given interval input earlier. Enter a non-real number to end the loop: "))
    print(interpolate(temp))
