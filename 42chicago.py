###Chicago###

import random
import sys
'''
games = 10 
for i in range(games):
	print(f'game#{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
			if d1 + d2 == target:
			print(f' yay, rolled {d1} anf {d2} for {target} points')	
games = 1000
for i in range(games):
	score = 0 
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score) # final game score

'''
games = 1000000 # 1 million trials   
log = games // 100 # report progress at 1% intervals
total = 0
zeroes = 0  
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
		if score == 0: zeroes += 1
		total += score
print(total / games)
print(zeroes / games)
