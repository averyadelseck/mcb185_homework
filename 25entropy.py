# Shannon Entropy
''' 
doc-strings:
For determining the shannon entropy for four nucleotides.
All nucleotides must occur once.
'''
import math

def entropy(a, c, g, t):
	if a > 0 and c > 0 and g > 0 and t > 0:
	return((a/(a + c + g + t) * math.log2(a/(a + c + g + t))) +
	 (c/(a + c + g + t) * math.log2(c/(a + c + g + t))) + 
	 (g/(a + c + g + t) * math.log2(g/(a + c + g + t)))
	  + (t/(a + c + g + t) * 
	 math.log2(t/(a my	+ c + g + t)))) 
	else: 									print('error: not all nucleotides occur once')

print(entropy(1, 2, 3, 4))

print(entropy(0, 0, 0, 4))
