# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab4A-Act2
# Date:         16 September 2026

arr2d = [[0, 0, 0], [1, 0, 0],
         [1, 1, 0], [1, 1, 1],
         [0, 1, 0], [0, 1, 1],
         [0, 0, 1], [1, 0, 1]
        ]

# Resolve a and b and c
for i in range(len(arr2d)):
    a = arr2d[i][0]; b = arr2d[i][1]; c = arr2d[i][2]
    print(f"Given a={a}, b={b}, c={c}, the expression \"a and b and c\" evaluates to: {a and b and c}")
print("---------------------------------------")

# Resolve a or b or c
for i in range(len(arr2d)):
    a = arr2d[i][0]; b = arr2d[i][1]; c = arr2d[i][2]
    print(f"Given a={a}, b={b}, c={c}, the expression \"a or b or c\" evaluates to: {a or b or c}")
print("---------------------------------------")

# Resolve (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
for i in range(len(arr2d)):
    a = arr2d[i][0]; b = arr2d[i][1]; c = arr2d[i][2]
    print(f"Given a={a}, b={b}, c={c}, the expression \"(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c)", end=" ")
    print(f"or (a and not b)\" evaluates to: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}")
print("---------------------------------------")

# Resolve (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
for i in range(len(arr2d)):
    a = arr2d[i][0]; b = arr2d[i][1]; c = arr2d[i][2]
    print(f"Given a={a}, b={b}, c={c}, the expression \"(not ((b or not c) and (not a or not c))) or (not (c or not (b and c)))", end=" ")
    print(f"or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))\" evaluates to:", end=" ")
    print(f"{(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}")
