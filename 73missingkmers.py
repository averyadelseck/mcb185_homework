import sys
import mcb185
import itertools


program = 'ecoli.fa.gz' #change later
kmermiss = []
for i in range(0, k):
	kcount = {}
	for defline, seq in mcb185.read_fasta(program):
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount:	kcount
			if kmer in kcount: 		kmermiss.append('kmer')

