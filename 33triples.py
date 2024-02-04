###triples 
'''
Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. Hint: all sides, including the hypotenuse, must be an integer.
'''
import math

a = 0
b = 1
for a in range(1, 100):
	a = a + 1
	for b in range(1, 100):
		c = (a**2 + b**2)**.5
		if math.isclose(c, c // 1): print(a, b, c)
	b = b + 1
	if c > 100: break


