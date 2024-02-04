###Unit 3 - demo
'''
while boolean expression is True>:
	do_something


while True:
	print('hello')

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 5: break


i = 0
while i < 3:
	print (i) 
	i = i + 2
print(i)
'''
for i in range(1, 10, 3):
	print('1', i)
	
for i in range(0, 5):
	print('2', i)

for char in 'avery':
	print(char)
	
seq = 'GAATC'
for nt in seq:
	print(nt)
'''
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
		'''
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:            print(nt1, nt2, '-1')
	
limit = 4
for i in range(1, limit):
	for j in range(i, limit):
		print(i, j+1)

limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
		
#Algorithms

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total
	
print(gc_comp('ACAGCGAAT'))

def maxchar(s):
	mx = 0
	for c in s:
		if ord(c) > mx:
			mx = ord(c)
	return mx
	
def minchar(n):
	minx = 256
	for c in n:
		if n < minx:
			mx = n
	return minx
	
print(minchar(8))
	
	
