import mcb185
import sys
import dogma

seq = sys.argv[1]
minlength = int(sys.argv[2])

def genefinder(seq, minlength):
	geneloc = []
	for frame in range(3):
		fseq = seq[frame:]
		i = frame
		while i < len(fseq):
			codon = fseq[i:i+3]
			if codon == 'ATG':
				start i 
				
				for j in range(i, len(fseq -2, 3):
					codon = fseq[j:j+3]
					if codon == 'TAA' or codon == 'TAG':
						stop j
						
						if len(fseq[start:stop]) >= minlength:
							geneloc.append((start, stop))
							
						i = stop
						break
			1 += 3
	return geneloc
	
for defline, seq in mcb185.read_fafsta(sys.argv[1]):
	antiseq = dogma.revcomp(seq)
	
	genloc_forward = genefinder(seq, minlength)
	for nt in geneloc_forward:
		print('+' nt[0], nt[1], '-')
		
	genloc_forward = genefinder(antseq, minlength)
	for nt in geneloc_forward:
		print('-' nt[0], nt[1], '-')
		
print(geneloc_forward)
print(geneloc_reverse)
print(len(genlocforward) + len(geneloc_reverse))

#coauthored
