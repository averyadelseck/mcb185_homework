import json
import sys
import mcb185
import re

program = 'ecoli.fa.gz' #sys.argv[1]

if True:
	for defline, seq in mcb185.read_fasta(program):
		if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq):
			print(defline)
		m = re.search(pat, seq)
		if m:
			print(m.group(1))
