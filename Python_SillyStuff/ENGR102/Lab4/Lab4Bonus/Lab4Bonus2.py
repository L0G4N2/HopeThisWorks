# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab4B-Bonus2
# Date:         16 September 2026

# 0 <= x <= 10: 10x
# 10 < x <= 60: 40x
# x > 60: f(x) = f(x - 1) - 1, where f(1) = 40
# When f(x) = 0, x = 0 (this will happen after 100 days have passed)

print("The widget-making machine will be most efficient after 10 days, but will start making one less widget per day after 60 days, and", end=" ")
print("stop producing widgets after 100 days.")
days = int(input("Enter the number of days (integer) the machine will be running: "))

widgets = 0
capOff = 40
if days >= 0 and not (days > 100):
    for i in range(days):
        i += 1
        if i <= 10:
            widgets += 10
        elif i > 10 and i <= 60:
            widgets += 40
        elif i == 100:
            print("The machine has ceased opperations...")
            break
        elif i > 60 and capOff != 0:
            capOff -= 1
            widgets += capOff
    print(f"After running for {days} days, the machine has made {widgets} widgets.")
else:
    print("You have entered an invalid number of days.")
