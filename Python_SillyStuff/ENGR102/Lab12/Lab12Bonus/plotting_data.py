# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   plotting_data
# Date:         16 November 2026

# Imports
import os, numpy as np, matplotlib.pyplot as plt

# Class to create objects of each row in the Weather Data and store their data inside of an object
class WeatherData:
    def __init__(self, line):
        self.date = line[0]
        self.avgDailyWindSpeed = line[1]
        self.percip = line[2]
        self.avgRelHumid = line[3]
        self.avgTemp = line[4]
        self.maxTemp = line[5]
        self.minTemp = line[6]
        if self.avgTemp == "No recorded data":
            self.avgTemp = str((float(self.maxTemp) + float(self.minTemp)) / 2)

    def getMonthAndYear(self):
        # Convert from numerical month to month name
        month, day, year = self.date.split('/')
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        monthName = months[int(month) - 1]
        return monthName, int(year)

def findMonthInYear(list, monthIn, yearIn):
    monthInYear = []
    for data in list:
        month, year = data.getMonthAndYear()
        if month == monthIn and year == yearIn:
            monthInYear.append(data)
    return monthInYear

# Use the file path to access the files
scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, 'WeatherDataCLL.csv')

# Open WeatherDataCLL.csv and create objects of each line in the file
with open(filePath, 'r') as file:
    line = file.readline(); line = file.readline().strip()  # Skip the header line
    line = list(line.split(','))  # Split the line into a list of values
    weatherDataList = []
    while line != [""]:
        for value in line:
            if value == "":
                line[line.index("")] = "No recorded data"
        weatherData = WeatherData(line)
        weatherDataList.append(weatherData)
        line = file.readline().strip()
        line = list(line.split(','))

# Create different arrays of values 
maximumTemps = np.array([]); minimumTemps = np.array([]); avgTemps = np.array([])
avgWindSpeeds = np.array([]); percipitations = np.array([]); avgRelHumidities = np.array([])
for data in weatherDataList:
    maximumTemps = np.append(maximumTemps, float(data.maxTemp)) if data.maxTemp != "No recorded data" else maximumTemps
    minimumTemps = np.append(minimumTemps, float(data.minTemp)) if data.minTemp != "No recorded data" else minimumTemps
    avgTemps = np.append(avgTemps, float(data.avgTemp)) if data.avgTemp != "No recorded data" else avgTemps
    avgWindSpeeds = np.append(avgWindSpeeds, float(data.avgDailyWindSpeed)) if data.avgDailyWindSpeed != "No recorded data" else avgWindSpeeds
    # percipitations = np.append(percipitations, float(data.percip)) if data.percip != "No recorded data" else percipitations
    # avgRelHumidities = np.append(avgRelHumidities, float(data.avgRelHumid)) if data.avgRelHumid != "No recorded data" else avgRelHumidities
    if data.percip != "No recorded data" and data.avgRelHumid != "No recorded data":
        percipitations = np.append(percipitations, float(data.percip))
        avgRelHumidities = np.append(avgRelHumidities, float(data.avgRelHumid))

# Setup the quad of graphs
plt.figure(figsize=(12, 10))

# Create this graph on the top left of the quad
axis1 = plt.subplot(2, 2, 1)

# Plot Max Temperatures on the left axis
maxTempDates = np.array(np.arange(len(maximumTemps)))
line1 = axis1.plot(maxTempDates, maximumTemps, color="red", label="Max Temp")
axis1.set_title("Maximum Temperature and Average Wind Speed")
axis1.set_xlabel("date"); axis1.set_ylabel("Maximum Temperature, F")

# Plot Average Wind Speeds on the right axis
avgWindSpeedsDates = np.array(np.arange(len(avgWindSpeeds)))
axis1Right = axis1.twinx()
line2 = axis1Right.plot(avgWindSpeedsDates, avgWindSpeeds, color="blue", label="Avg Wind")
axis1Right.set_ylabel("Average Wind Speed, mph")

# Combine the legends for both of these graphs
lines = line1 + line2
labels = [line.get_label() for line in lines]
axis1Right.legend(lines, labels, loc="lower left", framealpha=0.8, facecolor="white")

# Create this graph on the top right of the quad
axis2 = plt.subplot(2, 2, 2)

# Create the histogram of the Average Wind Speeds
plt.hist(avgWindSpeeds, bins=32, color="green", edgecolor="black")
plt.title("Histogram of Average Wind Speed")
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of days")

# Create this graph on the bottom left of the quad
plt.subplot(2, 2, 3)

# Create the scatterplot of Percipitation vs Average Relative Humidity
plt.scatter(avgRelHumidities, percipitations, color="black", s=10)
plt.title("Percipitation vs Average Relative Humidity")
plt.xlabel("Average Relative Humidity (%)")
plt.ylabel("Percipitation (in)")

# Create this graph on the bottom right of the quad
plt.subplot(2, 2, 4)

# Create the bar chart of the Temperatures by Month
monthlyAvgTemps = np.zeros(12); monthlyMaxTemps = np.zeros(12); monthlyMinTemps = np.ones(12) * 1000; monthlyCounts = np.zeros(12)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for data in weatherDataList:
    month, day, year = data.date.split('/')
    monthName = months[int(month) - 1]
    max = float(data.maxTemp) if data.maxTemp != "No recorded data" else 0
    min = float(data.minTemp) if data.minTemp != "No recorded data" else 1000
    for m in months:
        # if monthName == m:
            monthlyAvgTemps[int(month) - 1] += float(data.avgTemp) if data.avgTemp != "No recorded data" else 0
            monthlyCounts[int(month) - 1] += 1
            monthlyMaxTemps[int(month) - 1] = max if max > monthlyMaxTemps[int(month) - 1] else monthlyMaxTemps[int(month) - 1]
            monthlyMinTemps[int(month) - 1] = min if min < monthlyMinTemps[int(month) - 1] else monthlyMinTemps[int(month) - 1]

for i in range(12):
    monthlyAvgTemps[i] /= monthlyCounts[i]

months = np.array(np.arange(1, 13))
plt.bar(months, monthlyAvgTemps, color="y")

# Create lines for maximum and minimum temperatures
plt.plot(months, monthlyMaxTemps, color="red", label="High T")
plt.plot(months, monthlyMinTemps, color="blue", label="Low T")
plt.title("Temperature by Month")
plt.xlabel("Month"); plt.ylabel("Average Temperature, F")
plt.xticks(range(1, 13))
plt.legend(loc="upper right")

# Adjust graphs and titles, then show the graphs
plt.tight_layout(); plt.show()
