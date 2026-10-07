# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6B-Act2A
# Date:         29 September 2026

# Collatz Conjecture: 3n + 1, where n is a positive integer. If n is an even number, divide by 2, else, 3n + 1
print("Collatz Conjecture: 3n + 1, where n is a positive integer. If n is an even number, divide by 2, else, 3n + 1")
n = int(float(input("Enter a positive integer value: ")))
while n < 0:
    print("You have entered an incorrect value.")
    n = int(float(input("Enter a positive integer value: ")))

x = n
iterations = 0
while x != 1:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
    print(x)
    iterations += 1

print(f"When {n} is input into the Collatz Conjecture, it will take {iterations} steps to reach the value of 1.")
