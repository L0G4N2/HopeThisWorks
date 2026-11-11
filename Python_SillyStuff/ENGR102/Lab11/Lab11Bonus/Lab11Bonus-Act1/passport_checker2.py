# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   passport_checker2
# Date:         02 November 2026

import os

scriptDir = os.path.dirname(__file__)

def isValidPassport(passport, outfile):
    passport = passport.split()
    fields = [field.split(":")[0] for field in passport]
    values = [value.split(":")[1] for value in passport]
    passportDict = dict(zip(fields, values))

    byrValid = 1920 <= int(passportDict.get("byr", 0)) <= 2002
    iyrValid = 2013 <= int(passportDict.get("iyr", 0)) <= 2023
    eyrValid = 2023 <= int(passportDict.get("eyr", 0)) <= 2033
    heightCM = passportDict.get("hgt", "").endswith("cm") and 150 <= int(passportDict.get("hgt", "0cm")[:-2]) <= 193
    heightIN = passportDict.get("hgt", "").endswith("in") and 59 <= int(passportDict.get("hgt", "0in")[:-2]) <= 76
    hgtValid = heightCM or heightIN
    hclValid = passportDict.get("hcl", "").startswith("#") and len(passportDict.get("hcl", "")) == 7 and all(c in "0123456789abcdef" for c in passportDict.get("hcl", "")[1:])
    pidValid = len(passportDict.get("pid", "")) == 9
    cidValid = len(passportDict.get("cid", "")) == 3 and all(c in "123456789" for c in passportDict.get("cid", "")[0])
    isValid = byrValid and iyrValid and eyrValid and hgtValid and hclValid and pidValid and cidValid

    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "cid"]
    optionalField = "ecl"

    for field in requiredFields:
        if field not in passportDict:
            # print(f"Missing required field: {field}")
            # print("Passport:", passport)
            return False
    if isValid:
        outfile.write(" ".join(passport) + "\n\n")
        return True
    else:
        return False

file = input("Enter the name of the file: ")
infilePath = os.path.join(scriptDir, file)
outfilePath = os.path.join(scriptDir, "valid_passports2.txt")

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
