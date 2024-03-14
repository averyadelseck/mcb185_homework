import math

def transcribe(dna):
	return dna.replace('T', 'U')

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'UUU' or codon == 'UUC': 																			aas.append('F')
		elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':	aas.append('L')
		elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA': 														aas.append('I')
		elif codon == 'AUG': 																							aas.append('M')
		elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG': 										aas.append('V')
		elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC': 	aas.append('S')
		elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG': 										aas.append('P')
		elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG': 										aas.append('T')
		elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG': 										aas.append('A')
		elif codon == 'UAU' or codon == 'UAC': 																			aas.append('Y')
		elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA': 														aas.append('*')
		elif codon == 'CAU' or codon == 'CAC': 																			aas.append('H')
		elif codon == 'CAA' or codon == 'CAG': 																			aas.append('Q')
		elif codon == 'AAU' or codon == 'AAC': 																			aas.append('N')
		elif codon == 'AAA' or codon == 'AAG': 																			aas.append('K')
		elif codon == 'GAU' or codon == 'GAC': 																			aas.append('D')
		elif codon == 'GAA' or codon == 'GAG': 																			aas.append('E')
		elif codon == 'UGU' or codon == 'UGC': 																			aas.append('C')
		elif codon == 'UGG': 																							aas.append('W')
		elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG': 	aas.append('R')
		elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG': 										aas.append('G')
		else: continue
	return ''.join(aas)
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)
'''
def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)
'''
def gc_comp(seq): 
	#how many g/c are in the sequence
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

import math

seq = 'ACGTCGATTCGAT'
	
def entropy(seq):
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	bc = a + c + t + g
	if 'A' in seq and 'C' in seq and 'G' in seq and 'T' in seq and bc > 0:
		return ((a/(bc) * math.log2(a/(bc))) + (c/(bc) * math.log2(c/(bc))) + (g/(bc) * math.log2(g/(bc))) + (t/(bc) * math.log2(t/(bc))))
	else: return 0 

def avghydrobit(prot):
	tothb = 0
	hbs = []
	for aa in prot:
		if aa == 'I': 	hb = 4.5
		elif aa == 'V': hb = 4.2
		elif aa == 'L': hb = 3.8
		elif aa == 'F': hb = 2.8
		elif aa == 'C': hb = 2.5
		elif aa == 'M': hb = 1.9
		elif aa == 'A': hb = 1.8
		elif aa == 'G': hb = -0.4
		elif aa == 'T': hb = -0.7
		elif aa == 'S':	hb = -0.8
		elif aa == 'W': hb = -0.9
		elif aa == 'Y': hb = -1.3
		elif aa == 'P': hb = -1.6
		elif aa == 'H': hb = -3.2
		elif aa == 'E': hb = -3.5
		elif aa == 'Q':	hb = -3.5
		elif aa == 'D': hb = -3.5
		elif aa == 'N': hb = -3.5
		elif aa == 'K': hb = -3.9
		elif aa == 'R': hb = -4.5
		else: return 0
		hbs.append(hb)
		tothb += hb
	return tothb / len(hbs) 
