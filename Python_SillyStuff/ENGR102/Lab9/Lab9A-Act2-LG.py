# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab9A-Act2-LG
# Date:         20 October 2026

# Temporary varibale to snuff the error
coords = []

# Linear interpolation formula: y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
def interpolate(x):
    min_x = coords[0][0]
    max_x = coords[-1][0]

    # If x is exactly at an endpoint, return the corresponding y-value directly
    if abs(x - min_x) < 1e-9:
        return coords[0][1], "interpolation"
    if abs(x - max_x) < 1e-9:
        return coords[-1][1], "interpolation"

    # Find the interval containing x for interpolation
    for i in range(len(coords) - 1):
        x1 = coords[i][0]; x2 = coords[i + 1][0]
        y1 = coords[i][1]; y2 = coords[i + 1][1]

        if (x1 <= x <= x2) or (x2 <= x <= x1):
            y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
            return y, "interpolation"

    # If x is outside the interval, use the endpoints for extrapolation
    if x < min_x:
        x1 = coords[0][0]; x2 = coords[1][0]
        y1 = coords[0][1]; y2 = coords[1][1]
    else:
        x1 = coords[-2][0]; x2 = coords[-1][0]
        y1 = coords[-2][1]; y2 = coords[-1][1]

    y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
    return y, "extrapolation"
