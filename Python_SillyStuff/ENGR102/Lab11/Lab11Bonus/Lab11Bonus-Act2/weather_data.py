# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   weather_data
# Date:         03 November 2026

import os

scriptDir = os.path.dirname(__file__)

with open(os.path.join(scriptDir, 'weather_data.txt'), 'r') as file:
    line = file.readline(); line = file.readline()  # Skip the header line
    while line:
        
