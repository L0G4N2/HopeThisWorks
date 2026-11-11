# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   weather_data
# Date:         03 November 2026

import os

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

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, 'WeatherData.csv')

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
        # x = len(weatherDataList)

# Print the 10-Year maximum and minimum temperatures
maxTemp = 0; minTemp = 3000
for data in weatherDataList:
    try:
        temp = float(data.maxTemp)
        if maxTemp < temp:
            maxTemp = temp
    except:
        pass
    try:
        temp = float(data.minTemp)
        if minTemp > temp:
            minTemp = temp
    except:
        pass
print(f"10-year maximum temperature: {maxTemp}")
print(f"10-year minimum temperature: {minTemp}")

# Take user input of a month and year
month = input("Enter a month: ")
year = int(input("Enter a year: "))
print(f"For {month} {year}: ")
objList = findMonthInYear(weatherDataList, month, year)
# Finding the mean average daily temperature for Month in Year
sum = 0; count = 0; countForDays = 0
for obj in objList:
    if obj.avgTemp != "No recorded data":
        sum += float(obj.avgTemp)
        countForDays += 1
    count += 1
meanAvgTemp = sum / count
if countForDays > 0:
    print(f"Mean average daily temperature: {meanAvgTemp:.1f} F")
else:
    print(f"There was no data recorded for the average temperature in {month} {year}.")

# Finding the mean relative humidty for Month in Year
sum = 0; count = 0; countForDays = 0
for obj in objList:
    if obj.avgRelHumid != "No recorded data":
        sum += float(obj.avgRelHumid)
        countForDays += 1
    count += 1
meanAvgRelHumid = sum / count
if countForDays > 0:
    print(f"Mean relative humidty: {meanAvgRelHumid:.1f}%")
else:
    print(f"There was no data recorded for the relative humidity rate in {month} {year}.")

# Finding the mean daily wind speed for Month in Year
sum = 0; count = 0; countForDays = 0
for obj in objList:
    if obj.avgDailyWindSpeed != "No recorded data":
        sum += float(obj.avgDailyWindSpeed)
        countForDays += 1
    count += 1
meanAvgDailyWindSpeed = sum / count
if countForDays > 0:
    print(f"Mean daily wind speed: {meanAvgDailyWindSpeed:.2f} mph")
else:
    print(f"There was no data recorded for the average daily wind speed in {month} {year}.")

# Finding the mean percentage of days with percipitation for Month in Year
sum = 0; count = 0; countForDays = 0
for obj in objList:
    if obj.percip != "No recorded data" and obj.percip != "0":
        sum += 1
        countForDays += 1
    count += 1
percentPercip = (sum / count) * 100
if countForDays > 0:
    print(f"Percentage of days with percipitation: {percentPercip:.1f}%")
else:
    print(f"There was no data recorded for the amount of percipitation in {month} {year}.")
