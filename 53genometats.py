import gzip 
import sys
import math

'''
gffpath = sys.argv[1]
feature = sys.argv[2]
'''

lengths = []
count = 0
min = 0
max = 0
mean = 0
sd = 0
median = 0

searchterm = 'CDS'
print(searchterm)

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != searchterm: continue
		beg = int(words[3])
		end = int(words[4]) 
		cdlength = (end - beg + 1)
		lengths.append(cdlength)
		
		
if True:
	count = len(lengths) 
	print('count:', count) 
	mini = lengths[0]
	maxi = lengths[0]
	for length in lengths:
		if length < mini: min = length
		if length > max: max = length
	print('min: ', min)
	print('max: ', max)

if True:
	mean = 0
	total = 0
	for length in lengths:
		total = total + length 
		mean = total / count
	print('mean: ', mean)

if True:
	sd = 0
	dif = 0
	mu = 0
	for length in lengths:
		dif = (length - mean) ** 2
		mu = mu + dif
	sd = (mu / count) ** .5
	print('standard deviation: ', sd)
	
if True:
	pos = len(lengths)
	numb = 0.5 * pos
	if numb % 2 == 1.0:
		numb = int(numb)
		median = lengths[numb]
	else:
		top = int(numb + 0.5) 
		bottom = int(numb - .5)
		median = (lengths[top] + lengths[bottom]) / 2
	print('median:', median)

	
	
	

'''maybe and try and add the each of the variables after each of the functions

# create a new variables in each of the
def counts(lengths):
	lengths_count = len(lengths)
	return lengths_count
	print('length count: ', lengths_count)
 
def minmax(lengths):
	mini = lengths[0]
	max = lengths[0]
	for length in lengths:\
		if length < mini: min = length
		if length > max: max = length 
		print('min: ', min, 'max: ', max)
	return mini, max
	
def average(lengths):
	
	
	
	

Find:
+ Count 
+ min 
+ max 
+ sd
+ median

be able to swith between each of the files
'''

# to look up with with wifi: what is the function to count the number of items in a list, and find out if dropping th s is a correct and specific function part of it?
