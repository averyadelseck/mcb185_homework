'''
Write a program that predicts which proteins in a proteome are transmembrane.
Transmembrane proteins are characterized by having:

+ a hydrophobic signal peptide near the N-terminus
+ other hydrophobic regions to cross the plasma membrane

Hydrophobicity can be measured in many ways. We'll use Kyte-Doolittle for its
historical importance.

https://en.wikipedia.org/wiki/Hydrophilicity_plot

Here are the specifics of what the program is looking for in each sequence



For the E.coli proteome, your output should look something like this:

NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str
NP_414568.1 lipoprotein signal peptidase [Escherichia coli s
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Esch
NP_414607.1 DedA family protein YabI [Escherichia coli str.
NP_414609.1 thiamine ABC transporter membrane subunit [Esche
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr.
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia
NP_414695.1 iron(III) hydroxamate ABC transporter membrane s
NP_414699.1 PF03458 family protein YadS [Escherichia coli st
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str

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
					prots.apped(prot)	
	return prots	 
print(profinder(seq, 2))

# pulled from dogma 
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
		hbs.append(hb)
		tothb += hb
	return tothb / len(hbs) 

print(avghydrobit(prot))
prot = 'IIIIIIIIIIIICLFCMAGMCFIVSYAYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'

+ signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
+ transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
+ no prolines in either hydrophobic region
'''

#should work
#prot = 'IIIIIIIIIIIIICLFCMAGMCFIVSYAYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'
# Proline found
#prot = 'IIIIIIIIIIIIICLFCMAGMCFIVSYAPYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'
# No singal Peptide
#prot = 'RKNRKNRKRNRKNRKRNKRNRKRNRKNRKIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'
# No transmembrane Seq
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
		hbs.append(hb)
		tothb += hb
	return tothb / len(hbs) 


prot = 'IIIIIIIIIIIIICLFCMKRNRKNRKIMRQSFSYVYIMRNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNKNRKRN'

import dogma 

def tmfinder(prot):
	spcan = []
	finprot = []  
	sp = prot[:30]
	if 'P' in prot:
		return 'Proline found'
	for i in range(len(sp) -8 +1):
		ssp = sp[i:i+8]
		avhb = dogma.avghydrobit(ssp)
		print(i, avhb)
		if avhb >= 2.5: 
			spcan.append(ssp)
	
	for seq in spcan:
		tr = prot[:30]
		for j in range(len(tr) -11 +1):	
			seqtrans = tr[j:j+11]
			print(seqtrans)
			avhb = dogma.avghydrobit(seqtrans)
			print(j, avhb) 
			if avhb >= 2.0: 
				finprot.append(prot)
	return finprot

print(tmfinder(prot))
