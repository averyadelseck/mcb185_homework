### Unit 5 ### 
 
import math 
import sys
import random
import gzip
'''
# Indexes

seq = 'AVERY'
print('1x:')
print(seq[0], seq[3])
print('2x:')
print(seq[-1])
print('3x:')
for nt in seq:print(nt, end='')
print()
print('4x:')
for i in range(len(seq)):
	print(i,seq[i])
print('5x:')

# Slices

s = 'averyadelseck'
print('1x:')
print(s[0:3])
print('2x:')
print(s[0:8:2])
print('3x')
print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ
print(s, s[::], s[::1], s[::-1]) 

# Tuples

tax = ('Homo', 'sapiens', 9606)
print(tax)

s[0] = 'C'
tax[0] = 'human'

print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
	
x1, x2 = quadratic(5, 6, 1)

print('quadratic', x1, x2)

intercepts = quadratic(5, 6, 1)

print(intercepts[0], intercepts[1])

# Enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)):
	print('1x', i, nts[i])

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)): #len() returns the number of object in the list
	print('2x', nts[i], names[i])

for nt, names in zip(nts, names):
	print('3x', nt, names)

for i, (nt, name) in enumerate(zip(nts, names)):
	print('4x', i, nt, names)
	
# Lists
print('HI, LOOK HERE')
print()

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G' #switches out the original number with a new one
print(nts)

nts.append('C')  #adds somthig to the end of the list
print(nts)

last = nts.pop()  #list.pop() gets rid of things at the end of a list
print(last)


nts.sort()	#sort will sort items in a list, make sure not to mix them up with strings
print(nts)
nts.sort(reverse=True)
print(nts)

print()
print('new stuff')
nucleotides = nts 
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)	#if you renames something (x=y) then for any changes that you make to y you also make to x

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append('avery')
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph)
print(aas)
#split and join

text = 'my name is avery joy adelseck'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))	#the 'x' in the split shows us where to split into different items

print('look here', aas)
s = '-'.join(aas)  #puts the list back together with this in the middle of it
print(s)
s = ' '.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')	#this searched through the entirity of the list to see if there is a match

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

print('practice problems')
#Write a function that returns the minimum value of a list.
print('minimun value', ())

vals = '123456789'
vals = list(vals)

def minvalue(vals):
	mini = vals[0]   #the first value in the list is equal to the variable 'mini' 
	for val in vals[1:]: #for each value...
		if val < mini: mini = val #check if it is lower then the set value of mini then reset it
	return mini

	
#Write a function that returns both the minimum and maximum values of a list.

def min_max(vals):
	mini = vals[0]
	max  = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	for val in vals[1:]:			#after looking at the answer remember that if you are going through the same forloop, then you can simply condense them, there is no reason to diverge it
		if val > max: max = val
	return mini, max # I could also just use the sort value, and then return the bookends

#Write a function that returns the mean of the values in a list.

def men(vals):
	avg = 0
	for val in vals[1:]:
		avg += val 
	return total / len(vals)
#Write a function that computes the entropy of a probability distribution.

def entropy(probs):
	h = 0 
	for p in probs:
		h -= p * math.log2(p)
	return h 
print(entropy([0.2, 0.3, 0.5]))

#Write a function that computes the Kullback-Leibler distance between two sets of probability distributions.

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		 d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(dkl(p1, p2))

# Files

will open(path) as fp:
	for line in fp:
		do_something_with(line) #this will read through a file line by line
		
fp = open(path)
for lin in fp:
	do_somthing(line)
fp.close()

with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')

print('hello')
i = int('42')
x = float('0.61803')
# everytime you pull a number out of a file you have to convert it into a number. think about the difference between '1' and 1.
'''
#Practice Problems

vals = '123456789'
vals = list(vals)

#minimum
def minimum(vals):
	mini = vals[0]
	for val in vals:
		if val < mini: mini = val
	return mini
	print(mini)
	
print(minimum([1, 2, 3, 5]))

#minimum and maximum
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	print(mini, maxi)

print(minmax([2, 3, 5]))

#average 
def average(vals):
	sum = 0
	iter = 0
	for val in vals:
		sum = sum + val
		iter += 1
	average = sum / iter 
	return average 
	print('average')

print('average = ', average([2, 3, 5, 3, 2]))
	
def mean(vals):
	total = 0 
	for val in vals: total += val
	return total / len(vals)
	print(total / len(vals))
	print(mean)
	
print('mean = ', mean([2, 3, 5, 3, 2]))

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h 
print('entropy = ', entropy([0.2, 0.3, 0.5]))

