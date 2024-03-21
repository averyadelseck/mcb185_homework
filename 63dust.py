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
	print(discard)
	
w = 20
e = -1.4

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seq = seq[:40]
	if True:
		newdna = []
		discard = []
		for i in range(len(seq) -w +1):
			s = seq[i:i+w]
			if i == 0:
				ent = dogma.entropy(s) 
				if ent < e: 
					newdna.append(s)
				else: 
					discard.append(s)
			else:
				s = seq[i:i+w]
				ent = dogma.entropy(s) 
				if ent < e:
					newdna.append(seq[i])
				else: 
						discard.append(seq[i]) 
		print(defline[:30], newdna)
