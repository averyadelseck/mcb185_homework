# command line: python3 63dust.py ecoli.fa.gz 20 1.4

import dogma 
import sys
import math 
import mcb185

'''
plan:
for i in seq():
	create a windowing algorithm:
		count the shannon's entropy of each of them 
		if shanon's entropy above x: append the dna
		if not, do not append
'''
seq = 'ACGTCGATTCGAT'

# pulled from my dogma.py 
	
def entropy(seq):
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	bc = a + c + t + g
	if 'A' in seq and 'C' in seq and 'C' in seq and 'T' in seq and bc > 0:
		return ((a/(bc) * math.log2(a/(bc))) + (c/(bc) * math.log2(c/(bc))) + (g/(bc) * math.log2(g/(bc))) + (t/(bc) * math.log2(t/(bc))))
	else: return 0 


seq ='CGACAGGCATGCCCCCGATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATATATATATATATATATATATTATATTATATATATATTATATATCGATCGATCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGTCAGGGGGGCGACGGATATATTTAAAAAAACGGTACGCAATGCTACGGGGGGGGGGGG'
w = 20
e = -1.4
newdna = []
discard = []

def dust(seq):
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		if i == 0:
			ent = dogma.entropy(s) 
			print(ent)
			if ent < e: 
				newdna.append(s)
			else: 
				discard.append(s)
		else:
			s = seq[i:i+w]
			ent = dogma.entropy(s)
			print(ent) 
			if ent < e:
				newdna.append(seq[i])
			else: 
				discard.append(seq[i])
		
	print(newdna)
	print(discard)	
	
print(dust(seq)) 
