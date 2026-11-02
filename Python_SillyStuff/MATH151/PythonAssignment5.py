from sympy import *

theta = symbols("theta")

''' Law of Cosines:     d^2 = a^2 + b^2 - 2abcos(THETA)
    Length of hands:    Hour: 3in      Minute: 4in
                        d^2 = (3)^2 + (4)^2 - 2(3)(4)cos(THETA)
                        d^2 = 9 + 16 - 24cos(THETA)
                        d^2 = 25 - 24cos(THETA)
                        d = SQRT(25 - 24cos(THETA)
    Revolutions:        wH = 2PI rad / 720 min  wM = 2PI rad / 60 min
                        d(THETA) / dt = wH - wM
                                      = -11PI / 6 (rad / hr)
'''

# Problem 1
#print everything at the top!

# Problem 2 
# Compute  d distance / dt (with theta as 90 degrees)

