# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab4B-Bonus1
# Date:         16 September 2026

# Reyonolds Number (Re) is a dimensionless parameter and determines the flow of viscous forces
# Indicates whether the flow is laminar, turbulent, or in transition
# For flow in a pipe, the Reynolds Number is: Re = Vd / v
# Where V is the characteristic velocity (m/s), d is the diameter of the pipe (m), and v is the fluid kinematic viscosity (m^2/s)
charVel = float(input("Enter the characteristic velocity of the fluid: "))
diameter = float(input("Enter the diameter of the pipe the fluid is flowing through: "))
viscosity = float(input("Enter the fluid kinematic viscosity: "))
Re = (charVel * diameter) / viscosity

print(f"A fluid with a characteristic velocity of {charVel} m/s flowing through a pipe with a diameter of {diameter} m", end=" ")
print(f"and a kinematic viscosity of {viscosity} (m^2)/s has a Reynolds Number of: {Re:.8f}.")

if Re < 2300:
    print(f"The fluid is under laminar flow.")
elif Re > 2900:
    print(f"The fluid is under turbulent flow.")
else:
    print(f"The fluid is in transition from laminar to turbulent flow.")
