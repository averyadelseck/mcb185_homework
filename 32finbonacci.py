### Finbonacci
'''
classic programming interview question is to write a program that reports the first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21. This is a tricky problem. You need to initialize and keep track of 2 previous values.
'''
def fibonacci(n):
	fiba = 1
	fibb = 0
	fib = 0
	print(fibb)
	print(fiba)
	for i in range(0, 21):
		fib = fiba + fibb
		fibb = fiba
		fiba = fib
		print(fib)
print(fibonacci(0))
