## 20demo.py avery adelseck
print ("hello world") #greeting

"""
This is a 
multi-line
comment
"""
#math operators
print(1.5e-2)
print(1 + 1)
print("1"+"1")
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 +1))
"""
#functions
abs(x) #absolute power of x
pow(x, y) #x^y
round(x, ndigits=3) #round to n digitd

#functions pt. 2

make sure to input the math library before you do anything. remember when you did the coding thing over summer
"""

import math

a = 3
b = 4
c = math.sqrt(a** + b**2)
print(c)

#functions pt. 3

def greeting():
	print('hello yourself')

# ex.

def pythagoras(a, b):
	c - math.sqrt(a**2 + b**2)
	return c

print(0.1 * 1)
print(0.1 * 3)

# homework assignment

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')

#functions

def greeting():
	print('hello yourself')
def pythagoras (a,b):
	c = math.sqrt(a**2 +b**2)
	return c
x = pythagoras(3,4)
print(x)
#revised

def pythagoras (a,b):
        return  math.sqrt(a**2 +b**2)
x = pythagoras(3,4)
print(x)

print(pythagoras(1,0))


def pythagoras (a,b):
	if a <=0: sys.exit('error: a must be greater than 0')
	if b <=0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)

#practice

def negpos (a):
	return (-1*a)

print(negpos(3))
print(negpos(-3))

def tempctof (a):
	return (a * 9/5) + 32

print(tempctof(43))


def midpoint(x1, y1, x2, y2):
	mx=(x1+x2)/2
	my=(y1+y2)/2
	return mx, my
print(midpoint(3, 4, 5, 6)) 

#strings

s = 'hello world'
print(s, type(s))

#conditionals

a = 0.3
b = 0.1 * 3

if a == b:
	print('a equals b')
if a != b:
	print('a does not equal b')
print(a, b)

#boolean
c = a == b
print(c)
print(type(c))
print(a, b)

#if-elifl-else

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

#reformat

if a < b:	print('a < b 1')
elif a > b: print('a > b 1')
else:		print('a == b 1')

#note: equalities are rare, unless you mround the number

print(abs(a-b)) 
if abs(a-b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough')

#string comparison

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#more practice

s5=G
if s5==G:
	print('c')
elif s5==C:
	print('g')
elif s5==A:
	print('t')
elif s5==T:
	print('a')
else:
	sys.ext('unknown nucleotide')
