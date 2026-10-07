# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   Lab5A-Act2
# Date:         22 September 2026

# Create the cholesterol values for male and female
cholRange2dListM = [[0, 0, 0, 0, 0],
                    [4, 3, 2, 1, 0],
                    [7, 5, 3, 1, 0],
                    [9, 6, 4, 2, 1],
                    [11, 8, 5, 3, 1]
                   ]
cholRange2dListF = [[0, 0, 0, 0, 0],
                    [4, 3, 2, 1, 1],
                    [8, 6, 4, 2, 1],
                    [11, 8, 5, 3, 2],
                    [13, 10, 7, 4, 2]
                   ]

# Create the smoker values for male and female
smokerListM = [8, 5, 3, 1, 1]
smokerListF = [9, 7, 4, 2, 1]

# Create the systolic BP values for male and female
systBP2dListM = [[0, 0],
                 [0, 1],
                 [1, 2],
                 [1, 2],
                 [2, 3]
                ]
systBP2dListF = [[0, 0],
                 [1, 3],
                 [2, 4],
                 [3, 5],
                 [4, 6]
                ]

# Determine if the user is a male or female
isMale = None
while not (isMale == "M" or isMale == "F"):    
    isMale = input("Are you a male or female (M/F)? ").upper()
    if not (isMale == "M" or isMale == "F"):
        print("You have entered an invalid symbol.")
if isMale == "M":
    isMale = True
elif isMale == "F":
    isMale = False

# Test Cases for asking if the user is a male. Uncomment any one of the following lines to test for your specific test case:
# print(f"When \'M\' is input, is the user a male? {isMale})
# print(f"When \'m\' is input, is the user a male? {isMale})
# print(f"When \'F\' is input, is the user a male? {isMale})
# print(f"When \'f\' is input, is the user a male? {isMale})
# print(f"When \'L\' is input, is the user a male? {isMale})
# print(f"When \'0\' is input, is the user a male? {isMale})

# Determine the age of the user and setup the ageRange variable
age = int(float((input("Enter your current age from 20-80: "))))
ageRange = None
while age < 20 or age > 80:
    print("You have entered an invalid age, please try again. ")
    age = int(float(input("Enter your current age from 20-80: ")))

# Test Cases for asking for the users age. Uncomment any one of the following lines to test for your specific test case:
# print(f"When \'33\' is input, is 'age' equal to the test case?: {age == 33}")
# print(f"When \'20\' is input, is 'age' equal to the test case?: {age == 20}")
# print(f"When \'100\' is input, is 'age' equal to the test case?: {age == 100}")
# print(f"When \'15\' is input, is 'age' equal to the test case?: {age == 15}")
# print(f"When \'74.9\' is input, is 'age' equal to the test case?: {age == 74.9}")

# Retrieve the users' cholesterol level
cholesterol = int(float(input("Enter your current level of cholesterol: ")))

# Test Cases for asking for the users current cholesterol level. Uncomment any one of the following lines to test for your specific test case:
# print(f"When \'230\' is input, is \'cholesterol\' equal to the test case? {cholesterol == 230}")
# print(f"When \'280\' is input, is \'cholesterol\' equal to the test case? {cholesterol == 280}")
# print(f"When \'1000000000000\' is input, is \'cholesterol\' equal to the test case? {cholesterol == 1000000000000}")
# print(f"When \'-20\' is input, is \'cholesterol\' equal to the test case? {cholesterol == -20}")

# Determine if the user is a smoker or not
isSmoker = None
while not (isSmoker == "Y" or isSmoker == "N"):
    isSmoker = input("Do you currently smoke (Y/N)? ").upper()
    if not (isSmoker == "Y" or isSmoker == "N"):
        print("You have entered an invalid symbol.")
if isSmoker == "Y":
    isSmoker = True
elif isSmoker == "N":
    isSmoker = False

# Test Cases for asking if the user is a smoker. Uncomment any one of the following lines to test for your specific test case:
# print(f"When \'Y\' is input, is the user a smoker? {isSmoker}")
# print(f"When \'y\' is input, is the user a smoker? {isSmoker}")
# print(f"When \'N\' is input, is the user a smoker? {isSmoker}")
# print(f"When \'n\' is input, is the user a smoker? {isSmoker}")
# print(f"When \'2\' is input, is the user a smoker? {isSmoker}")
# print(f"When \'P\' is input, is the user a smoker? {isSmoker}")

# Determine the users HDL level
hdl = int(float(input("Enter your current HDL in terms of mg/dL: ")))

# Test Cases for asking the users' HDL. Uncomment any one of the following lines and enter the proper value(s) to test:
# print(f"When \'45\' is input, is \'hdl\' equal to the test case? {hdl == 45}")
# print(f"When \'40\' is input, is \'hdl\' equal to the test case? {hdl == 40}")
# print(f"When \'59.999\' is input, is \'hdl\' equal to the test case? {hdl == 59.999}")
# print(f"When \'39\' is input, is \'hdl\' equal to the test case? {hdl == 39}")

# Determine the users Systolic BP
systBP = int(float(input("Enter your current Systolic Blood Pressure in terms of mmHg: ")))

# Test Cases for asking the users' Systolic Blood Pressure. Uncomment any one of the following lines and enter the proper value(s) to test:
# print(f"When \'138\' is input, is \'systBP\' equal to the test case? {systBP == 138}")
# print(f"When \'120\' is input, is \'systBP\' equal to the test case? {systBP == 120}")
# print(f"When \'100\' is input, is \'systBP\' equal to the test case? {systBP == 100}")
# print(f"When \'170\' is input, is \'systBP\' equal to the test case? {systBP == 170}")
# print(f"When \'160\' is input, is \'systBP\' equal to the test case? {systBP == 160}")

isTreated = None
while not (isTreated == "Y" or isTreated == "N"):
    isTreated = input("Has this been treated (Y/N)? ").upper()
    if not (isTreated == "Y" or isTreated == "N"):
        print("You have entered an invalid symbol.")
if isTreated == "Y":
    isTreated = 1
elif isTreated == "N":
    isTreated = 0

# Test Cases for asking the user if they are receiving blood pressure treatment. Uncomment any one of the following lines and enter the proper value(s) to test:
# print(f"When \'N\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")
# print(f"When \'n\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")
# print(f"When \'Y\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")
# print(f"When \'y\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")
# print(f"When \'L\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")
# print(f"When \'45\' is input, is the user recieving blood pressure treatment? {bool(isTreated)}")

# Calculate the number of Farmington Points the user has based on the following conditionals:
if isMale:
    # Set the base number of points the male user has based on their age
    if age <= 34 and age >= 24:
        points = -9
        ageRange = 0
    elif age <= 39 and age >= 35:
        points = -4
        ageRange = 0
    elif age <= 44 and age >= 40:
        points = 0
        ageRange = 1
    elif age <= 49 and age >= 45:
        points = 3
        ageRange = 1
    elif age <= 54 and age >= 50:
        points = 6
        ageRange = 2
    elif age <= 59 and age >= 55:
        points = 8
        ageRange = 2
    elif age <= 64 and age >= 60:
        points = 10
        ageRange = 3
    elif age <= 69 and age >= 65:
        points = 11
        ageRange = 3
    elif age <= 74 and age >= 70:
        points = 12
        ageRange = 4
    elif age <= 79 and age >= 75:
        points = 13
        ageRange = 4

    # Add points based on the users cholesterol level
    if cholesterol < 160:
        points += 0
    elif cholesterol <= 199 and cholesterol >= 160:
        points += cholRange2dListM[1][ageRange]
    elif cholesterol <= 239 and cholesterol >= 200:
        points += cholRange2dListM[2][ageRange]
    elif cholesterol <= 279 and cholesterol >= 240:
        points += cholRange2dListM[3][ageRange]
    elif cholesterol >= 280:
        points += cholRange2dListM[4][ageRange]

    # Add points based on whether the user is a smoker or not
    if isSmoker:
        points += smokerListM[ageRange]
    else:
        points += 0

    # Add points based on the users HDL
    if hdl >= 60:
        points += -1
    elif hdl <= 59 and hdl >= 50:
        points += 0
    elif hdl <= 49 and hdl >= 40:
        points += 1
    elif hdl < 40:
        points += 2

    # Add points based on the users Systolic BP
    if systBP < 120:
        points += 0
    elif systBP <= 129 and systBP >= 120:
        points += systBP2dListM[1][isTreated]
    elif systBP <= 139 and systBP >= 130:
        points += systBP2dListM[2][isTreated]
    elif systBP <= 159 and systBP >= 140:
        points += systBP2dListM[3][isTreated]
    elif systBP >= 160:
        points += systBP2dListM[4][isTreated]

    # Calculate Ten-year Risk
    if points <= 4:
        tenYrRisk = 1
    elif points == 5 or points == 6:
        tenYrRisk = 2
    elif points == 7:
        tenYrRisk = 3
    elif points == 8:
        tenYrRisk = 4
    elif points == 9:
        tenYrRisk = 5
    elif points == 10:
        tenYrRisk = 6
    elif points == 11:
        tenYrRisk = 8
    elif points == 12:
        tenYrRisk = 10
    elif points == 13:
        tenYrRisk = 12
    elif points == 14:
        tenYrRisk = 16
    elif points == 15:
        tenYrRisk = 20
    elif points == 16:
        tenYrRisk = 25
    elif points >= 17:
        tenYrRisk = 30
elif isMale == False:
    # Set the base number of points the female user has based on their age
    if age <= 34 and age >= 24:
        points = -7
        ageRange = 0
    elif age <= 39 and age >= 35:
        points = -3
        ageRange = 0
    elif age <= 44 and age >= 40:
        points = 0
        ageRange = 1
    elif age <= 49 and age >= 45:
        points = 3
        ageRange = 1
    elif age <= 54 and age >= 50:
        points = 6
        ageRange = 2
    elif age <= 59 and age >= 55:
        points = 8
        ageRange = 2
    elif age <= 64 and age >= 60:
        points = 10
        ageRange = 3
    elif age <= 69 and age >= 65:
        points = 12
        ageRange = 3
    elif age <= 74 and age >= 70:
        points = 14
        ageRange = 4
    elif age <= 79 and age >= 75:
        points = 16
        ageRange = 4

    # Add points based on the users cholesterol level
    if cholesterol < 160:
        points += 0
    elif cholesterol <= 199 and cholesterol >= 160:
        points += cholRange2dListF[1][ageRange]
    elif cholesterol <= 239 and cholesterol >= 200:
        points += cholRange2dListF[2][ageRange]
    elif cholesterol <= 279 and cholesterol >= 240:
        points += cholRange2dListF[3][ageRange]
    elif cholesterol >= 280:
        points += cholRange2dListF[4][ageRange]

    # Add points based on whether the user is a smoker or not
    if isSmoker:
        points += smokerListF[ageRange]
    else:
        points += 0

    # Add points based on the users HDL
    if hdl >= 60:
        points += -1
    elif hdl <= 59 and hdl >= 50:
        points += 0
    elif hdl <= 49 and hdl >= 40:
        points += 1
    elif hdl < 40:
        points += 2

    # Add points based on the users Systolic BP
    if systBP < 120:
        points += 0
    elif systBP <= 129 and systBP >= 120:
        points += systBP2dListF[1][isTreated]
    elif systBP <= 139 and systBP >= 130:
        points += systBP2dListF[2][isTreated]
    elif systBP <= 159 and systBP >= 140:
        points += systBP2dListF[3][isTreated]
    elif systBP >= 160:
        points += systBP2dListF[4][isTreated]

    # Calculate Ten-year Risk
    if points <= 12:
        tenYrRisk = 1
    elif points == 13 or points == 14:
        tenYrRisk = 2
    elif points == 15:
        tenYrRisk = 3
    elif points == 16:
        tenYrRisk = 4
    elif points == 17:
        tenYrRisk = 5
    elif points == 18:
        tenYrRisk = 6
    elif points == 19:
        tenYrRisk = 8
    elif points == 20:
        tenYrRisk = 11
    elif points == 21:
        tenYrRisk = 14
    elif points == 22:
        tenYrRisk = 17
    elif points == 23:
        tenYrRisk = 22
    elif points == 24:
        tenYrRisk = 27
    elif points >= 25:
        tenYrRisk = 30

# Print the users 10-year risk
print(f"Your ten-year risk is at: {tenYrRisk}%")

# Test Cases for the users' 10-Year Risk. Uncomment any one of the following lines and enter the proper value(s) to test:
# print(f"When \'m, 34, 150, n, 50, 100, n\' are input into the program respectively, is the ten-year risk 1%? {tenYrRisk == 1}")
# print(f"When \'f, 34, 150, n, 50, 100, n\' are input into the program respectively, is the ten-year risk 1%? {tenYrRisk == 1}")
# print(f"When \'m, 59, 180, y, 30, 180, y\' are input into the program respectively, is the ten-year risk 30%? {tenYrRisk == 30}")
# print(f"When \'f, 59, 180, y, 30, 180, y\' are input into the program respectively, is the ten-year risk 17%? {tenYrRisk == 17}")
# print(f"When \'m, 60, 239, n, 40, 132, n\' are input into the program respectively, is the ten-year risk 12%? {tenYrRisk == 12}")
# print(f"When \'f, 60, 239, n, 40, 132, n\' are input into the program respectively, is the ten-year risk 3%? {tenYrRisk == 3}")
