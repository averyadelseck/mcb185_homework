# fizzbuzz

'''prompt: One of the classic interview questions is FizzBuzz. Make a program that writes out the numbers from 1 to 100. If the number is  ivisible by 3, write Fizz instead. If the number is divisible by 5, write Buzz instead. If the number is divisible by both 3 and 5, write FizzBuzz.'''

for i in range(0, 101):
	if i == 0: print('Welcome to my fizzbuzz  code')
	if i in range(0, 101, 15): print(i, 'fizzbuzz')
	elif i in range(0, 101, 3): print(i, 'fizz')
	elif i in range(0, 101, 5): print(i, 'buzz')
	else: print(i)
	if i == 100: break
