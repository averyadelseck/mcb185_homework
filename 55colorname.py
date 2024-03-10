import sys 
import math
import gzip

#just take the W for now then come back later

# colorfile = sys.argv[1]

R = sys.argv[1]
G = sys.argv[2]
B = sys.argv[3]


def dtc(P, R):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d


path = '../MCB185/data/colors_extended.tsv'
reds = []
greens = []
blues = [] 

with open(path) as fp:
	reds = []
	greens = []
	blues = [] 
	for line in fp:
	 	words = line.split()
	 	numbers = words[2]
	 	code = numbers.split(',')
	 	r = code[0]
	 	g = code[1]
	 	b = code[2]
	 	if r == R and g == G and b == B:
	 		print(line)
	 	else: continue
	 	difr = R - r
	 	difg = G -g
	 	difb = B - b
	reds.append(difr)
	greens.append(difg)
	blues.append(difb)
	
	 
'''	for words[2] in fp:
	 		colors = line.split(',')
	 		print(colors)

		


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
