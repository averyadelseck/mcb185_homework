# Oligo Melting Temperature
def oligomeltt(A, T, G, C):
	if A + G + G + C < 13:	return (A + T) * 2 + (G + C) * 4
	else:					return 64.9 + 41 * (G + C - 16.4) / (A + T + G +C)
	
print(oligomeltt(1, 2, 3, 4))
print(oligomeltt(10, 11, 12, 13))
