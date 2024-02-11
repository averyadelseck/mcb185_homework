### DnD Stats ###

import math
import random
import sys



### Rolling 3 6-sided dice ###
games = 100000
stat = 0
for i in range(games):
	x = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) 
	stat = x + stat
print('3D6 =', stat / games)


### Roll 3 six-sided dice, but re-roll any 1s ###
games = 100000
stat = 0
for i in range(games):
	x = random.randint(2, 6) + random.randint(2, 6) + random.randint(2, 6)
	stat = x + stat
	#troubleshoot: print('x=', x,'stat=', stat)
print('3D6r1 =', stat / games)


### roll pairs of six-sided 3 times, taking the maximum each time ###
games = 100000
stat = 0
for i in range(games):
	x1 = random.randint(1, 6)
	x2 = random.randint(1, 6)
	if x1 > x2: x = x1
	else:       x = x2
	y1 = random.randint(1, 6)
	y2 = random.randint(1, 6)
	if y1 > y2: y = y1
	else:       y = y2
	z1 = random.randint(1, 6)
	z2 = random.randint(1, 6)
	if z1 > z2: z = z1
	else:       z = z2
	stat = x + y + z + stat
	#troubleshoot: print('x=', x,'y=', y,'z=', z,'stat=', stat)
print('3D6x2 =', stat / games)


### 4D6d1: roll 4 six-sided dice, dropping the lowest die roll ###

games = 100000
stat = 0
min = 0
for i in range(games):
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	z = random.randint(1, 6)
	w = random.randint(1, 6)
	min = x
	if x > y: y = min
	if min > z: z = min
	if min > w: w = min
	stat = stat + x + y + z + w - min
	#troubleshoot: print('x=', x,'y=', y,'z=', z,'w=', w,'min=' , min,'stat=', stat)
print('3D6dl =', stat / games)
