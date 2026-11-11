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
            outfile.write(" " * int(p))
        else:
            outfile.write(char * int(p))
        index += 1

file = input("Enter the filename: ")
char = input("Enter a character: ")
infilePath = os.path.join(scriptDir, file)
outfilePath = os.path.join(scriptDir, "pixel_triangle.txt")

with open(infilePath, 'r') as infile, open(outfilePath, 'r+') as outfile:
    lines = infile.readlines()
    for line in lines:
        paintPixel(line.strip(), char, outfile)
        if line != lines[-1]:
            outfile.write("\n")
