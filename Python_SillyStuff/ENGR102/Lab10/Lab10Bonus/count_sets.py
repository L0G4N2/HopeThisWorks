# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   count_sets
# Date:         29 October 2026

def count_sets(n):
    limit = int(n**0.5)
    count = 0
    sets = []
    for a in range(0, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                remainder = n - a * a - b * b - c * c
                if remainder >= c * c:
                    d = int(remainder**0.5)
                    if d * d == remainder:
                        sets.append([a, b, c, d])
                        count += 1
    return count, sets

# how to measure how long your function takes to run:
while True:
    temp = int(input("Num: "))
    count, sets = count_sets(temp)
    print(f"There are {count} different variations of four numbers that add up to {temp} when squared.")
    print(f"Those sets are: {sets}")
