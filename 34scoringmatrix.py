###Scoring Matrix

nts = 'ACGT'
plus = '+1'
minus = '-1'
# print header 
print('  ', end= '   ')
for nt in nts:
	print(nt, end= '  ')
print()

# print body
for nt1 in nts:
	print(nt1, end= ' ')
	for nt2 in nts:
		if nt1 == nt2: print(plus, end=' ')
		else:          print(minus, end='  ')
	print()
