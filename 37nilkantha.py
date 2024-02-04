### Nilkantha estimation of pi ###


a = 1
b = 2
c = 3
d = 4
pia = 3
for i in range(0, 101):
	pi = pia + a * (4 / (b * c * d))
	a = a * -1
	b = b + 2
	c = c + 2
	d = d + 2
	print(pi, a, b, c, d)
print('this is my estimation of pi: ', pi)
