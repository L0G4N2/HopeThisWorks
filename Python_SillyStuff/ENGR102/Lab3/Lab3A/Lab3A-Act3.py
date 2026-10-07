# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab3B-2
# Date:         8 September 2026

# This program takes 5 input to create a short madlibs story
animal = input("Name an animal (singular): ")
name = input("Enter the name of any person: ")
adjective = input("Enter an adjective (a descriptive word): ")
age = int(input("Enter a number from 10-20: "))
country = input("Name of a country: ")

months = age * 12

print(f"There once was a {animal} named {name} who was very {adjective}. They told me they were {age} old and that they were still very young.", end=" ")
print(f"I asked them if they knew how to do math and they replied, \"Of course, I can tell you my age in months to prove it, too!\"", end=" ")
print(f"There was no way they could do so, it\'s unheard of, but I heard them out anyway. \"I am {months} months old,\" they exclaimed, \"all you have to do is multiply my age in years by 12!\"", end=" ")
print(f"\tWhoa\t I couldn\'t believe they actually knew that. I asked them where they went to school at, and you know what they said?\n{country}\tBecause of course they did.")
