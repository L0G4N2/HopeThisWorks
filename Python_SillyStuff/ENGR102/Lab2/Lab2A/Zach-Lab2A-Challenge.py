# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
# Names: 
# Daniel Vicari 738004466
# Zachary Adams 637008110
# Harshil Patel 838007668
# Logan Gutierrez 737008832
# Section: 555
# Assignment: Lab2A-1
# Date: 01 09 2026

# Input value for time
input_time = 1200

# Observed positions
pos_1 = 50
pos_2 = 615

# Observed times
time_1 = 30
time_2 = 45

# Racetrack length 
track_length = 500

# Calculated constant speed
speed = (pos_2-pos_1)/(time_2-time_1)

# Calculated initial position at time 0
pos_initial = pos_1-speed*time_1

# Calculating position at a specific input time
calculated_pos = speed*input_time+pos_initial

# Calculating full laps around the track
full_laps = calculated_pos//track_length

# Calculating total distance travelled across full laps
full_laps_dist = full_laps*track_length

# Calculating distance past the finish line on the current lap
dist_past_line = calculated_pos-full_laps_dist

# Printing Outputs
print("Time = ",input_time,"seconds","    Position = ",dist_past_line,"meters")
print("These values represent the position of a racecar (in meters) past the starting line on a 500 meter racetrack at 20 minutes after the observer arrives at the racetrack")

