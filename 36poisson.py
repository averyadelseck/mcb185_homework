### Poission Probabilities
''' 
Create a function that computes the Poisson probability of k events occuring with an expectation of n (n^k e^-n / k!) and demonstrate it works by calling it with several values of n and k.
'''
import math

def poission(n, k):
	pois = (((n**k) * (math.e)**(-n)) / math.factorial(k))
	print(pois)

print(poission(6, 2))
print(poission(8, 71))
print(poission(59, 73))
print(poission(4, 80))
print(poission(1,5))
