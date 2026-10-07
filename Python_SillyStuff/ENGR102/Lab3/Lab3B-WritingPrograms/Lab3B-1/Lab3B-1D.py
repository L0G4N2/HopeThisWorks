# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab3B-1D
# Date:         8 September 2026

from math import *

# Queuing Theory: M/M/1 Queue where a system has a single queue.
# The mean number of packets in the system is: p / (1 - p), where p is: lamda / mu
# The average queue length is: p^2 / (1 - p)
# lamda is the rate at which packets arrive (packets per second) and mu is the rate at which packets may be served (packets per second)
arrivalRate = float(input("Enter the rate at which the packets arrive in packets per second: "))
serviceRate = float(input("Enter the rate at which the packets are served in packets per second: "))

# Create new variable p and assign its value as the ratio of arrival rate to service rate
p = arrivalRate / serviceRate

# Solve for the mean number of pacckets in the system
meanNumber = p / (1 - p)

# Solve for the average length of the queue
averageLen = pow(p, 2) / (1 - p)

# Print the result of the equation and truncate at 8 decimal places
print(f"The mean number of packets in a M/M/1 queue with an arrival rate of {arrivalRate} packets per second and a service rate of {serviceRate} packets per second is: {meanNumber:.8f}")
print(f"The average length of packets in the queue of this system is: {averageLen:.8f}")
