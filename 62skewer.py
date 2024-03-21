import dogma 
import mcb185
import math
import sys


def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0 
	return (g-c) / (g + c)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

seq = 'ACGTACGTGGG'
w = 3
gccount = []
oldgc = seq[0]
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seq = seq[:40]
	for i in range(len(seq) -w +1): # for each iteration from the #of dna molecules - the window + 1
		s = seq[i:i+w]
		if i == 0: 
			gc = dogma.gc_comp(s)
			gccount.append(gc) 
		else:
			newgc = dogma.gc_comp(s)
			gccount.append(newgc)
print(gccount)

# I hope you dont care that I made it a list, I though it was probably better anyways.  
