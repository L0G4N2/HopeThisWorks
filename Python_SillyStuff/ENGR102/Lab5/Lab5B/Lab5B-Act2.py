# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab5B-Act2
# Date:         22 September 2026

# Youngs Modulus = stress / strain              Is in ksi
# Stress = Applied Force / Area                 Is in ksi
# Strain = Change in Length / Original Length   Is Unitless

# Retrieve the stress and strain from the user
print("This program returns the value of stress based on the value of strain entered by the user.")
print("The number returned is expected to be any number from 0-60, and will return \"None\" if the inputted", end=" ")
print("strain is beyond the fracture point.")
strain = -1
while strain < 0:
    strain = float(input("Enter the strain the material is undergoing as a real number from 0 to 0.3: "))
    if strain < 0:
        print("You have entered an invalid value.")

# Point A: (0.0125, 42 ksi)
# Point B: Point A
# Point C: (0.05703, 43 ksi)
# Point D: (0.18125, 60 ksi)
# Point E: (0.2625, 51 ksi)

# Linear interpolation formula: y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
# Where y values represent stress, and x values represent strain
x = strain; x1 = None; x2 = None
y = None; y1 = None; y2 = None

# Variable to define the area
areaIndex = None

# List of strings defining the outputs
areaList = ["in Area 0-A,B", "in Area A,B-C", "in Area C-D", "in Area D-E", "beyond the Fracture Point"]

# Solving for Stress using Linear Interpolation
if strain <= 0.0125:
    x1 = 0; x2 = 0.0125
    y1 = 0; y2 = 42
    areaIndex = 0
    # Test Case for Portion O to A,B. Uncomment and enter an appropriate value to test
    # print("Greetings from Bracket 0 to Point A,B!")

elif strain <= 0.05703:
    x1 = 0.0125; x2 = 0.05703
    y1 = 42; y2 = 43
    areaIndex = 1
    # Test Case for Portion A,B to C. Uncomment and enter an appropriate value to test
    # print("Greetings from Bracket A,B to Point C!")

elif strain <= 0.18125:
    x1 = 0.05703; x2 = 0.18125
    y1 = 43; y2 = 60
    areaIndex = 2
    # Test Case for Portion C to D. Uncomment and enter an appropriate value to test
    # print("Greetings from Bracket C to Point D!")

elif strain <= 0.2625:
    x1 = 0.18125; x2 = 0.2625
    y1 = 60; y2 = 51
    areaIndex = 3
    # Test Case for Portion D to E. Uncomment and enter an appropriate value to test
    # print("Greetings from Bracket D to Point E!")

elif strain > 0.2625:
    areaIndex = 4
    # Test Case for the fracture point. Uncomment and enter an appropriate value to test
    # print("Fracture Point!")

# Calculates only if the steel is not beyond its fracture point
if not (strain > 0.2625):
    y = f"{y1 + ((x - x1) * (y2 - y1)) / (x2 - x1):.8f}"
print(f"The value of stress when strain is equal to {x} will be, {y} ksi, and is {areaList[areaIndex]}.")

# Test Cases to check if strain is storing the correct number. Uncomment any one of the following and enter the appropriate value to test.
# print(f"When 0 is input, is strain equal to 0.0? {strain == 0.0}")
# print(f"When 0.001 is input, is strain equal to 0.001? {strain == 0.001}")
# print(f"When 0.0125 is input, is strain equal to 0.0125? {strain == 0.0125}")
# print(f"When 0.0126 is input, is strain equal to 0.0126? {strain == 0.0126}")
# print(f"When 0.03 is input, is strain equal to 0.03? {strain == 0.03}")
# print(f"When 0.05703 is input, is strain equal to 0.05703? {strain == 0.05703}")
# print(f"When 0.05704 is input, is strain equal to 0.05704? {strain == 0.05704}")
# print(f"When 0.1 is input, is strain equal to 0.1? {strain == 0.1}")
# print(f"When 0.18125 is input, is strain equal to 0.18125? {strain == 0.18125}")
# print(f"When 0.18126 is input, is strain equal to 0.18126? {strain == 0.18126}")
# print(f"When 0.2 is input, is strain equal to 0.2? {strain == 0.2}")
# print(f"When 0.2625 is input, is strain equal to 0.2625? {strain == 0.2625}")
# print(f"When 0.2626 is input, is strain equal to 0.2626? {strain == 0.2626}")
# print(f"When 0.1 is input, is strain equal to 0.1? {strain == 0.1}")
# If these all test cases are all true, the code runs as it should because that means that the correct value is being used for interpolation.
