###nchoosek


def fac(n):
	a = 1
	b = 1
	for n in range(0, n, 1):
		fac =  a * b
		a = fac
		b = b + 1
	print(fac)
		
print(fac(5))
		
'''		
def nck(n, k):
	prob = ( n ) / (k * (n - k)!
'''
