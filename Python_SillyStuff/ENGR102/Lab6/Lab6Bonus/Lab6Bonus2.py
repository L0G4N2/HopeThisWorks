# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6Bonus2
# Date:         30 September 2026

# Prime numbers can only be divided by themselves and 1
# Even numbers are divisible by 2

print("This program prints out whether numbers from 2 to 100 are prime of even, and does not print composite numbers.")

print("2 is prime")
for i in range(3, 101):
    if i % 2 == 0:
        print(f"{i} is not prime")
    else:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
            if count > 2:
                break
        if count == 2:
            print(f"{i} is a prime number")
