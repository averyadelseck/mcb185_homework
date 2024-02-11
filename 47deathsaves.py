### Death Saves 
import random
import math
import sys


succ = 0
fail = 0
rev = 0
for i in range(6):
	x = random.randint(1, 20)
	if x == 20: rev += 1
	elif x == 1: fail += 2
	elif x > 10: succ += 1
	else:      fail += 1
	print(x, succ, fail, rev)
	if rev == 1: print('Are you Jesus, because you just came back from the dead')
	if rev == 1: break
	if fail == 3: print('GAMEOVER, try your luck another day')
	if fail == 3: break
	if succ == 3: print('Hanging on for dear life') 
	if succ == 3: break


games = 100000
# inputs
succ = 0
fail = 0
rev = 0
# outcome totals
dead = 0
stable = 0
alive = 0

for i in range(games):
	x = random.randint(1, 20)
	if x == 20: rev += 1
	elif x == 1: fail += 2
	elif x > 10: succ += 1
	else:      fail += 1
	if rev == 1:
		alive += 1
		fail = 0
		succ = 0
		rev = 0
	if fail == 3: 
		dead += 1
		fail = 0
		succ = 0
		rev = 0
	if succ == 3: 
		stable += 1
		fail = 0
		succ = 0
		rev = 0
	
peralive = alive / (dead + alive + stable)
perdead = dead / (dead + alive + stable)
perstable = stable / (dead + alive + stable)

print(perdead)
print(peralive)
print(perstable)
print(perdead + perstable + peralive) #should equal 1 if everything is correct


