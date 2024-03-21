import sys 
import math
import gzip

#just take the W for now then come back later

# colorfile = sys.argv[1]

R = 0 #int(sys.argv[1])
G = 130 #int(sys.argv[2])
B = 185 #int(sys.argv[3])

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d


path = '../MCB185/data/colors_extended.tsv'

with open(path) as fp:
	totaldiff = 1000000000000000 
	
	for line in fp:
		print(line)
		words = line.split()
		numbers = words[2]
		code = numbers.split(',')
		r = int(code[0])
		g = int(code[1])
		b = int(code[2])
		
		diffr = dtc([R], [r])
		diffg = dtc([G], [g])
		diffb = dtc([B], [b])	
		
		difftot = diffr + diffg + diffb

		if difftot < totaldiff:
			totaldiff = difftot
			color = words[0]	 	
print('the color is:', color)

'''
# for absolute colors, I did this first, then the other one.
	for line in fp:
	 	words = line.split()
	 	numbers = words[2]
	 	code = numbers.split(',')
	 	color = words[0]
	 	r = code[0]
	 	g = code[1]
	 	b = code[2]
	 	if r == R and g == G and b == B:
	 		print(color)
	 

		


To search for items in containers, you can use `in`, `find()`, and `index()`.

The keyword `in` reads particularly well in conditional statements.

```python
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
```

The `index()` method returns the index of the first element it finds. If it
can't find a matching item, the function throws an error.

```python
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
```


The `find()` method returns the index of the first element it finds or a -1 if
it can't be found. This very useful behavior only works for strings, and not
tuples or lists.

```python
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
```

If you are searching a list or tuple, and you don't know if the element is
in the list, first use `in`.

```python
if thing in list: idx = list.index(thing)
```
'''
