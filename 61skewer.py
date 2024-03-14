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


seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1): # for each iteration from the #of dna molecules - the window + 1
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))
