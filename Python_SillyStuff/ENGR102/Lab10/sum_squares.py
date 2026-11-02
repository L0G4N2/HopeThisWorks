# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   sum_squares
# Date:         28 October 2026

from math import isqrt
from time import time

def list_nums(n):
    limit = isqrt(n)
    for a in range(0, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                remainder = n - a * a - b * b - c * c
                if remainder >= c * c:
                    d = isqrt(remainder)
                    if d * d == remainder:
                        return [a, b, c, d]

# how to measure how long your function takes to run:
while True:
    t1 = time() # get start time
    temp = int(input("Num: "))
    print(list_nums(temp)) # run function
    t2 = time() # get end time
    print(f"This took {t2-t1} seconds") # print result
