# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   pixel_painter
# Date:         02 November 2026

import os

scriptDir = os.path.dirname(__file__)

def paintPixel(pixel, char, outfile):
    pixel = pixel.split(",")
    index = 0
    for p in pixel:
        if index % 2 == 0:
            print(" " * int(p), end="", file=outfile)
        else:
            print(char * int(p), end="", file=outfile)
        index += 1
    print(file=outfile)

file = input("Enter the filename: ")
char = input("Enter a character: ")
infilePath = os.path.join(scriptDir, file)
outfilePath = os.path.join(scriptDir, "pixel_triangle.txt")

with open(infilePath, 'r') as infile, open(outfilePath, 'r+') as outfile:
    lines = infile.readlines()
    for line in lines:
        paintPixel(line.strip(), char, outfile)
