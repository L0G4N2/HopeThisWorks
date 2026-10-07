# First set of positions and time
x1 = 50
y1 = 0
time1 = 30

# Second set of positions and time
x2 = 615
y2 = 0
time2 = 45

# Calculate the speed of the car
distanceBetweenPositions = x2 - x1
timeBetweenPositions = time2 - time1
speed = distanceBetweenPositions / timeBetweenPositions

# Calculate the position of the car before the first time (30 seconds)
carTraveledInTime1 = speed * time1
carOriginToTrack = carTraveledInTime1 - x1

# Calculate the position of the car at a given time between 30 and 45 seconds
time3 = int(input("Enter the time (in seconds) to calculate the position of the object: "))
distTraveled = (speed * time3) - carOriginToTrack

# Linear interpolation formula: y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
y = y1 + ((distTraveled - x1) * (y2 - y1)) / (x2 - x1)

# Print speed and position of the car at a given time between 30 and 45 seconds
print(f"The speed of the object is: {speed:.2f} meters per second")
print(f"The position of the object at time {time3} is: ({distTraveled:.2f}, {y:.2f}), or {distTraveled:.2f} meters past the starting line on the track.")
