### Monte Carlo Estimate of pi ###

import math
import sys
import random 


pi = 0
inside = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	d = (x**2) + (y**2)
	print(d, x, y)
	if d <= 1:	
		inside += 1
		total += 1
	else:
		total += 1
	pi = 4 * (inside /(total))
	print(pi)		
