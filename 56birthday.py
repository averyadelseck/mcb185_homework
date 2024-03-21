import random
import sys


days = 2 #int(sys.argv[1])
people = 2 #int(sys.argv[2])
trials = 2 #int(sys.argv[3])

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


'''
import sys
import random

csize = int(sys.argv[1]) #chromosome size - number of days
rsize = int(sys.argv[2]) #amount o
rnum = int(sys.argv[3])

# create an empty chrom
chrom = []
for i in range(csize): chrom.append(0) 

# fill up the chrom with reads

for i in range(rnum): 
	pos = random.randint(0, csize-rsize)
	for j in range(rsize):
		chrom[pos+j] += 1
print(chrom)

# min coverage

min = rnum
for n in chrom[rsize:-rsize]:
	if n < min: min = n
print(min)
	
#window
k = 15
seq = 'AGCTGATCGATGAGCTAGCTAGC'
print(seq)
for i in range(0, len(seq) - k + 1, 1): #the 3 shows how much you skip by, you can hard code 3
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (c + g)/k)

'''
