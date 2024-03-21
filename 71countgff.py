import sys
import gzip

file = 'ecoli.gff.gz' #switch to sys.argv[0] b4 turning in

count = {}
with gzip.open(file, 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1 
	for f, n in count.items(): print(f, n)

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
	
