# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab6B-Act2A
# Date:         29 September 2026

temp = 0
average = 0
maximum = 0
minimum = 0
print("This program takes a user input of measurements in an infinite loop", end=" ")
print("and prints the average of the measurements after the user enters a negative value.")
while not (temp < 0):
    temp = float(input("Enter a measurement. Negative numbers will cancel the loop and print the average of the measurements: "))
    maximum = temp if temp >= maximum else maximum
    minimum = temp if temp <= minimum else minimum
    if not (temp < 0):
        average += temp
average /= 2
print(f"The average of the entered measurements is: {average}")
