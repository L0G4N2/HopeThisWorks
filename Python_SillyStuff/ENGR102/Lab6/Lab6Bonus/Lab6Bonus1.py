# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6Bonus1
# Date:         29 September 2026

# Program 1A

print("This program takes a user input of a positive integer and returns the sum", end = " ")
print("of every number from 0 to the entered number using a for loop and while loop.")

# Take the user input
x = int(input("Enter a positive integer value: "))
sumFor = 0
for i in range(0, x + 1):
    sumFor += i
print(f"This is the sum of every number from 0 to {x} using a for loop: {sumFor}")

sumWhile = 0
count = 0
while count != x + 1:
    sumWhile += count
    count += 1
print(f"This is the sum of every number from 0 to {x} using a while loop: {sumWhile}\n")

# Program 1B

print("This program takes the previous input of a positive integer and returns the product", end = " ")
print("of every number from 1 to the entered number using a for loop and while loop.")

proFor = 1
for i in range(1, x + 1):
    proFor *= i
print(f"This is the product of every number from 1 to {x} using a for loop: {proFor}")

proWhile = 1
count = 1
while count != x + 1:
    proWhile *= count
    count += 1
print(f"This is the product of every number from 1 to {x} using a while loop: {proWhile}")
