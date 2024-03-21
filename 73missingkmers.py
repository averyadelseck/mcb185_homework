import sys
import mcb185
import itertools


program = 'ecoli.fa.gz' #change later


kcount = {}
notkcount = {}
misskcount = {}


for defline, seq in mcb185.read_fasta(program):
	for k in range(0, 8):
		foundkmer = False
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount:	
				misskcount[kmer] = 0
				misskcount[kmer] += 1
				foundkmer = True
				break
		if not foundkmer:
			break

for kmner, count in misskcount.items():
	print(kmner, count)		
