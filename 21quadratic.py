##The Quadratic Formula Calculator

import math
'''
user guide:
in format: 0 = ax^2 + bx + c 
'''
def quadratic(a, b, c):
	x = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
	y = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
	return(x, y)
print(quadratic(3, -5, -8))
