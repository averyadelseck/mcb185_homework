#Kyte-Doolittle Hydrophobicity
'''
user guide:
enter 1 letter code for amino acid and get the hydrophobicity constant
'''
def hydrophobicity(s):
	if s == 'A': 	print('1.80')
	elif s == 'C':	print('2.50')
	elif s == 'D':	print('-3.50')
	elif s == 'E':	print('-3.50')
	elif s == 'F':	print('2.80')
	elif s == 'G':	print('-.40')
	elif s == 'H':	print('-3.20')
	elif s == 'I':	print('4.50')
	elif s == 'K':	print('-3.90')
	elif s == 'L':	print('3.80')
	elif s == 'M':	print('1.90')
	elif s == 'N':	print('-3.50')
	elif s == 'P':	print('-1.60')
	elif s == 'Q':	print('-3.50')
	elif s == 'R':	print('-4.50')
	elif s == 'S':	print('-0.80')
	elif s == 'T':	print('-0.70')
	elif s == 'V':	print('4.20')
	elif s == 'W':	print('-0.90')
	elif s == 'Y':	print('-1.30')
	else:			print('unknown nucleotide')	

print(hydrophobicity('A'))
print(hydrophobicity('B'))
