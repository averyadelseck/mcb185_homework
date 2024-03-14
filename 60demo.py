import sys
import mcb185
'''
Let's modify your program so that it counts 5 nucleotides (ACGTN), not just Cs
and Gs. One way to solve this problem is to create individual variables for
each nucleotide and a stack of if-elif-else statements that assigns them
individually.

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	G = 0 
	C = 0
	T = 0
	A = 0
	N = 0
	for nt in seq:
		if nt == 'A':	A += 1
		elif nt == 'C':	C += 1
		elif nt == 'G':	G += 1
		elif nt == 'T':	T += 1
		else:			N += 1
	print('G =',G / len(seq),'C =', C / len(seq),'T =', T / len(seq),'A =', A / len(seq),'N =', N / len(seq))

nts = 'ACGTN' 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	counts = []
	for i in range(len(nts)): counts.append(0)
	for nt in seq:
		if nt == 'A':	counts[0] += 1
		if nt == 'C':	counts[1] += 1
		if nt == 'G':	counts[2] += 1
		if nt == 'T':	counts[3] += 1
		else:			counts[4] += 1
	print(name, end='\t')
	print(counts[0]/len(seq)), 
	for n in counts: print(f'{n/len(seq):.4f}', end='\t') #\t is the tab key
	print()
	
# counting w/ str.count
nts = 'ACGTN'

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print() 


w = 10 #shows the window
s = 1 # shows the step size
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
'''

nts = 'ACGTN' 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc += 1
	print(name, gc/len(seq))
