##The Quadratic Formula Calculator

import math

def quadratic(a, b, c):
""" (a, b, c) are found from 0 = ax^2 + bx + c """
	x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
	x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
	return(x1, x2)

print(quadratic(3, -5, -8))
pyt
