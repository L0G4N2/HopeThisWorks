# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   barcode_checker
# Date:         02 November 2026

import os

scriptDir = os.path.dirname(__file__)

def checkBarcode(barcode):
    barcode = list(barcode)
    lastDig = barcode.pop()
    firstGroup = barcode[::2]
    secondGroup = barcode[1::2]
    sum1 = sum([int(dig) for dig in firstGroup])
    sum2 = sum([int(dig) for dig in secondGroup])
    lastDigCheck = 10 - ((sum1 + (sum2 * 3)) % 10)
    return lastDig == str(lastDigCheck)

file = input("Enter the name of the file: ")
infilePath = os.path.join(scriptDir, file)
outfilePath = os.path.join(scriptDir, "valid_barcodes.txt")

count = 0
with open(infilePath, "r") as infile, open(outfilePath, "r+") as outfile:
    barcode = infile.readline().strip()
    while barcode:
        if checkBarcode(barcode):
            outfile.write(barcode + "\n")
            count += 1
        barcode = infile.readline().strip()

print(f"There are {count} valid barcodes.")
