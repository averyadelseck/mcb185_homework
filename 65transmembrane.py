import dogma 
import mcb185
import math
import sys

#These are the trial sequences for cutting bugs
#should work
prot = 'IIIIIIIIIIIIICLFCMAGMCFIVSYAYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIIIIIIIII'
# Proline found
#prot = 'IIIIIIIIIIIIICLFCMAGMCFIVSYAPYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'
# No singal Peptide
#prot = 'RKNRKNRKRNRKNRKRNKRNRKRNRKNRKIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'
# No transmembrane Seq
'''
This is what I added to dogma, for refrence :)
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
'''

#prot = 'IIIIIIIIIIIIICLFCMKRNRKNRKIMRQSFSYVYIMRNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNNRNRNRNRNRNKNRKRN'

import dogma 

def tmfinder(prot):
	spcan = []
	finprot = []  
	sp = prot[:30]
	flag = False
	if 'P' in prot:
		return 'Proline found'
		
	for i in range(len(sp) -8 +1):
		ssp = sp[i:i+8]
		avhb = dogma.avghydrobit(ssp)
		if avhb >= 2.5: 
			spcan.append(ssp)
			flag = True
	if flag:
		for seq in spcan:
			tr = prot[:30]
			for j in range(len(tr) -11 +1):	
				seqtrans = tr[j:j+11]
				avhb = dogma.avghydrobit(seqtrans) 
				if avhb >= 2.0: 
					if not finprot:
						finprot.append(prot)

	if flag: print(finprot)

prot = 'IIIIIIIIIIIIICLFCMAGMCFIVSYAYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIIIIIIIII'
print(tmfinder(prot))

 
