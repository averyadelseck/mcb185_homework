##Random DNA Generator ###

import math
import random

nts = 'ACGT'

for i in range(0, 10):
	print()
	print(f'>seq-{i + 1}')
	print()
	for nts in range(50):
		print(random.choice('ACGT'), end='')
