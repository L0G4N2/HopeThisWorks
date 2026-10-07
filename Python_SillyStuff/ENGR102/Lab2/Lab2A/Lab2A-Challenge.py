import math

# Formula for the arc length of a circle: s = r * theta, where s is the arc length, r is the radius, and theta is the angle in radians
# Given the arc length and the radius, we can solve for theta: theta = s / r

# Radius of the racetrack in meters
radius = 0.5 * 1000

# First positions and times
arcLength1 = 50
time1 = 30
# Calculate the angle in radians for the first position
theta1 = arcLength1 / radius
# Position of the car in Cartesian coordinates (x, y) using polar to Cartesian conversion
x1 = radius * math.cos(theta1)
y1 = radius * math.sin(theta1)

# Second positions and times
arcLength2 = 615
time2 = 45
# Calculate the angle in radians for the second position
theta2 = arcLength2 / radius
# Position of the car in Cartesian coordinates (x, y) using polar to Cartesian conversion
x2 = radius * math.cos(theta2)
y2 = radius * math.sin(theta2)

# Calculate the speed of the car: w = (theta2 - theta1) / (time2 - time1), where w is the angular speed in radians per second
angularSpeed = (theta2 - theta1) / (time2 - time1)
linearSpeed = angularSpeed * radius

# Calculate the position of the car at any given time
time3 = float(input("Enter the time (in seconds) to calculate the position of the car: "))

# Position of the car in Cartesian coordinates (x, y) using polar to Cartesian conversion
theta = theta1 + angularSpeed * (time3 - time1)
lapCounter = int(theta / (2 * math.pi))
distanceFromStart = (theta * radius) % (2 * math.pi * radius)
x = radius * math.cos(theta)
y = radius * math.sin(theta)

# Print the speed and position of the car in Cartesian coordinates
print(f"The angular speed of the car is: {angularSpeed:.2f} radians per second.")
print(f"The linear speed of the car is: {linearSpeed:.2f} meters per second.")
print(f"The position of the car in Cartesian coordinates is: ({x:.2f}, {y:.2f}) after completing {lapCounter} full lap(s) around the track.")
print(f"The distance (arc length) traveled by the car is: {distanceFromStart:.2f} meters.")

# Test cases:
# Test case 1: time3 = 30
# Expected position: The position of the car in Cartesian coordinates is: (497.50, 49.92)
# Expected linear speed: The linear speed of the car is: 37.67 meters per second.
# Expected arc length (distance traveled): The distance (arc length) traveled by the car from the start is: 50.00 meters.
# Expected laps: The car has completed 0 laps

# Test case 2: time3 = 45
# Expected position: The position of the car in Cartesian coordinates is: (167.12, 471.24)
# Expected linear speed: The linear speed of the car is: 37.67 meters per second.
# Expected arc length (distance traveled): The distance (arc length) traveled by the car from the start is: 615.00 meters.
# Expected laps: The car has completed 0 laps

# Test case 3: time3 = 1200
# Expected position: The position of the car in Cartesian coordinates is: (481.16, 135.97)
# Expected linear speed: The linear speed of the car is: 37.67 meters per second.
# Expected arc length (distance traveled): The distance (arc length) traveled by the car from the start is: 137.70 meters.
# Expected laps: The car has completed 14 laps

# Test case 4: time3 = 37
# Expected position: The position of the car in Cartesian coordinates is: (404.80, 293.49)
# Expected linear speed: The linear speed of the car is: 37.67 meters per second.
# Expected arc length (distance traveled): The distance (arc length) traveled by the car from the start is: 313.67 meters.
# Expected laps: The car has completed 0 laps