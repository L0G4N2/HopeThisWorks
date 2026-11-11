# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   passport_checker
# Date:         02 November 2026

import os

scriptDir = os.path.dirname(__file__)

def isValidPassport(passport, outfile):
    passport = passport.split()

    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "cid"]
    optionalField = "ecl"

    for field in requiredFields:
        if field not in [field.split(":")[0] for field in passport]:
            # print(f"Missing required field: {field}")
            # print("Passport:", passport)
            return False
    outfile.write(" ".join(passport) + "\n\n")
    return True

file = input("Enter the name of the file: ")
infilePath = os.path.join(scriptDir, file)
outfilePath = os.path.join(scriptDir, "valid_passports.txt")
count = 0

with open(infilePath, "r") as infile, open(outfilePath, "r+") as outfile:
    passport = ""
    line = infile.readline()
    while line:
        if line == "\n" or line == "":
            isValid = isValidPassport(passport, outfile)
            passport = ""; count += 1 if isValid else 0
        else:
            passport += line
        line = infile.readline()
    isValid = isValidPassport(passport, outfile)
    count += 1 if isValid else 0

print(f"There are {count} valid passports")
