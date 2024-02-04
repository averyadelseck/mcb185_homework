###nchoosek


def fac(n):
	a = 1
	b = 1
	for i in range(0, n, 1):
		fac =  a * b
		a = fac
		b = b + 1
	print(fac)
		
print(fac(5))

''' 
At this point that I realized that we already have a function for factorials, so I do the rest of the problem with the one provided not my homemade one. 	
'''

import math

def nck(n, k):
	if n < k: print('incorrect input')
	c = n-k
	x= (math.factorial(n)) / (math.factorial(k) * math.factorial(c))
	print(x)
	
print(nck(9, 5))


'''
def nck(n, k):
	if n < k: print('incorrect input')
	c = n-k
	x= (fac(n)) / (fac(k) * fac(c))
	print(x)
	
print(nck(9, 5))
'''
