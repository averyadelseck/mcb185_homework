## Entropy ##

import sys
import math

'''
Calculates the Entropy according to a list of probabilities
[1] = The Probabilitys 
'''

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
	probs.append(float(arg))

total = 0 
for p in probs: total += p
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs:
	h -= p * math.log2(p)

print(h)
