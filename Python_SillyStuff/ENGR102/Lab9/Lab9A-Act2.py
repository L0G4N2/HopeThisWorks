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
print("This program prompts the user to enter a set of (x, y) coordinates and then repeatedly asks", end=" ")
print("for an x-value to calculate linear interpolation or extrapolation depending on where the x-value", end=" ")
print("lies relative to the entered interval. The program continues until the user enters a non-real number.")

# Lists that store the users coordinates and the existing x's
coords = []
existingXs = []

# Retrieve coordinates from the user and ensure no repeated x-values are entered
while True:
    try:
        numPoints = int(float(input("Enter the number of points that will be input (as an integer and min.2): ")))
        if numPoints >= 2:
            break
        print("Please enter an integer that is at least 2.")
    except:
        print("That is not a valid integer. Please try again.")

count = 0
while count < numPoints:
    try:
        x = float(input(f"Enter x-value #{count + 1} as a real number: "))
        y = float(input(f"Enter y-value #{count + 1} as a real number: "))
    except:
        print("Invalid numeric input. Please enter real numbers only.")
        continue

    if any(abs(existingX - x) < 1e-9 for existingX in existingXs):
        print("You cannot repeat x-values. Please enter a valid set of coordinates.")
        continue

    coords.append([x, y])
    existingXs.append(x)
    count += 1

coords.sort()

# Linear interpolation formula: y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
def interpolate(x):
    min_x = coords[0][0]
    max_x = coords[-1][0]

    # If x is exactly at an endpoint, return the corresponding y-value directly
    if abs(x - min_x) < 1e-9:
        return coords[0][1], "interpolation"
    if abs(x - max_x) < 1e-9:
        return coords[-1][1], "interpolation"

    # Find the interval containing x for interpolation
    for i in range(len(coords) - 1):
        x1 = coords[i][0]; x2 = coords[i + 1][0]
        y1 = coords[i][1]; y2 = coords[i + 1][1]

        if (x1 <= x <= x2) or (x2 <= x <= x1):
            y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
            return y, "interpolation"

    # If x is outside the interval, use the endpoints for extrapolation
    if x < min_x:
        x1 = coords[0][0]; x2 = coords[1][0]
        y1 = coords[0][1]; y2 = coords[1][1]
    else:
        x1 = coords[-2][0]; x2 = coords[-1][0]
        y1 = coords[-2][1]; y2 = coords[-1][1]

    y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
    return y, "extrapolation"

# Prompt the user to enter x until a non-real input is entered
while True:
    try:
        temp = float(input("Enter a real number as an x-value to interpolate/extrapolate on the given interval. Enter a non-real number to end the loop: "))
    except:
        print("Non-real input detected. Ending the program.")
        break

    result, method = interpolate(temp)

    if method == "interpolation":
        print(f"Since the x-value, {temp}, is between the entered coordinates, the linear interpolation will be: {result}")
    else:
        print(f"Since the x-value, {temp}, is outside of the entered coordinates, the linear extrapolation will be: {result}")
