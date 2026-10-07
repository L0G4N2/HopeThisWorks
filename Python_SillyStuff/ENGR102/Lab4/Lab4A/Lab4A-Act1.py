# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
# Names: 
# Daniel Vicari 738004466
# Zachary Adams 637008110
# Harshil Patel 838007668
# Logan Gutierrez 737008832
# Section: 555
# Assignment: Lab4A-Program1
# Date: 17 09 2026

from math import *

# Computation 1
var_1 = sin(pi/7)
var_2 = sqrt(var_1)
var_3 = sqrt(var_2)
var_4 = var_3**4
var_5 = var_4/sin(pi/7)
print(f"Computation 1: {var_5}")
real_val1 = 1
bool_1 = var_5==real_val1

# Computation 2
var_6 = 1/19 * sin(pi/5.978)
var_7 = var_6**(1/7)
var_8 = var_7**(4/7)
var_9 = var_8**(49/4)
var_10 = var_9 / sin(pi/5.978)
print(f"\nComputation 2: {var_10}")
real_val2 = 1/19
bool_2 = var_10==real_val2

# Computation 3 
var_11 = 1.00000000000
var_12 = 1.00000000001
var_13 = var_11 - var_12
var_14 = 1/var_13
var_15 = 1/var_14
var_16 = var_14 * var_15
var_17 = var_16**10000000000000000
print(f"\nComputation 3: {var_17}")
real_val3 = 1
bool_3 = var_17==real_val3

# Printing Statements
print(f"\nIs computation 1 equal to the value that it should be (1)?: {bool_1}")
print(f"\nIs computation 2 equal to the value that it should be (1/19)?: {bool_2}")
print(f"\nIs computation 3 equal to the value that it should be (1)?: {bool_3}")
