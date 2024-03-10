import random
import sys


days = int(sys.argv[1])
people = int(sys.argv[2])
trials = int(sys.argv[3])

matches = 0

for i in range(trials):
	calendar = []
	for j in range(days): calendar.append(0) 

	print()
	for j in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1

	max = 0
	for n in calendar[::]:
		if n > max: max = n
	
	if max > 1: matches += 1
	print(i / trials)

print(matches / trials)
