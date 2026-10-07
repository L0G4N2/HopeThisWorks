# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6B-Act2A
# Date:         29 September 2026

print("This program calculates what numbers divide a certain number from 2 to 100 evenly.")
for i in range(2, 101, 1):
    for j in range(2, i + 1):
        if i % j == 0:
            print(f"{j} divides {i}")
