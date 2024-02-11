### Saving Throw ###
### sorry, I do not know how to rename documents
import math
import random 
import sys

# Difficulty Class: 5
def dc(m):
	games = 10000000	
	stat = 0
	safe = 0
	dead = 0
	for i in range(games):
		for j in range(20):
			y = random.randint(1, 20) 
			if y > m: safe += 1 
			else:     dead += 1
	return(safe / (safe + dead))

print(dc(5))
print(dc(10))
print(dc(15))

'''

|  Difficulty Class	| Probability of Survival
|:------------------|:-----------------------
|		 5			|			.75
| 		10			|			.50
|		15			|			.25
|:------------------|:-----------------------
'''
