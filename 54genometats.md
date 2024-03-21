path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4]) 
		cdlength = (end - beg + 1)
		lengths.append(cdlength)




| Genome         | Type |  N   | Min |  Max  | Mean | Stdv | Med  |
|:---------------|:-----|:-----|:----|:------|:-----|:-----|:-----|
| A.thaliana     | gene | 4494 |  54 |  7077 | 899  | 644  | 1944 |
|                | exon |  207 |  58 |  2905 | 250  | 562  | 1490 |
|                | CDS  | 4337 |  54 |  7077 | 928  | 634  | 850  |
| C.elegans      | gene | 4494 |  54 |  7077 | 899  | 644  | 1944 |
|                | exon |  207 |  58 |  2905 | 562  | 562  | 1490 |
|                | CDS  | 4337 |  54 |  7007 | 2070 | 1435 | 1892 |
| D.melanogaster | gene | 4494 |  54 |  7077 | 899  | 644  | 1944 |
|                | exon |  207 |  58 |  2905 | 250  | 562  | 1490 |
|                | CDS  | 4337 |  54 |  7077 | 928  | 634  | 850  |
