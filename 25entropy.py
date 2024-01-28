# Shannon Entropy
''' 
prompt: Write a function that returns the Shannon entropy for nucleotide counts a, c,
g, t. Demonstrate it works using multiple calls, including those where one of
the counts is zero.
'''
import math

def avery(a):
	return a * math.log2(a) + a * math.log2(a)
print(avery(4))


def entropy(a, c, g, t):
	if a > 0 and c > 0 and g > 0 and t > 0: return ((a/(a + c + g + t) * math.log2(a/(a + c + g + t))) + (c/(a + c + g + t) * math.log2(c/(a + c + g + t))) + (g/(a + c + g + t) * math.log2(g/(a + c + g + t))) + (t/(a + c + g + t) * math.log2(t/(a + c + g + t)))) 
	else: 									print('error')

print(entropy(1, 2, 3, 4))

print(entropy(0, 0, 0, 4))
