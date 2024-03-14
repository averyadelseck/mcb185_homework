'''
+ Must perform a six-frame translation
+ Proteins must be at least 100 amino acids long
+ Proteins must start with 'M' and end with '*'
+ Deflines must have unique identifiers
'''	

import dogma 
import sys
import mcb185

seq = 'TACTAAATGTACACGTAGCTAAUGGACTGACGCATCGACTACGGACTGCACTACGACTCTGCTAGCTGATCGATCGGGCTGGCGGGATAGGGCTAAATTTTCGGGGAAAACGTGATCGACTGCATCGATCGATCGACG'

#tac = atg = aug = m

def profinder(seq, minprot):
	prots = translate3(seq, minprot)
	antiprots = translate3(mcb185.anti_seq(seq), minprot)
	return prots + antiprots

def translate3(seq, minprot):
	prots = []
	for rf in range(3):
		mrna = dogma.transcribe(seq[rf:])
		aaseq = dogma.translate(mrna)
		orfs = aaseq.split('*')
		for orf in orfs:
			if 'M' in orf:
				i = orf.index('M')
				prot = orf[i:]
				if len(prot) >= minprot:
					prots.append(prot)	
	return prots	 
print(profinder(seq, 2))
