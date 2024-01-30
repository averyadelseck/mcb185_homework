##The Quadratic Formula Calculator

import math

'''
doc-strings:
in format: 0 = ax^2 + bx + c 
'''

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
	x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
	return(x1, x2)

print(quadratic(3, -5, -8))
