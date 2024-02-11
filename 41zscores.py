### Z scores ###

import random

for i in range(5):
	r = (random.gauss(0.0, 20.0))
	if r > 5:   print('z > 0')
	if r > 10:  print('z = 1')
	if r > 15:  print('z = 2')
	else:       print('z < 0')


z1 = 0 
z2 = 0
z3 = 0
limit = 10
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z1/limit)
print(1 - 2*z3/limit)

