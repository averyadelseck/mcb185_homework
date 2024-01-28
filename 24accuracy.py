#Accuracy and F1 Score for Values


'''
user guide:
a = true positives 1
b = false positives 2
c = true negatives 3
d = false negatives 4
'''

def accuracy(a, b, c, d):
	return (a + c)/(a + b + c + d)

def f1(a, b, c, d):
	return ((2 * (a/(a + b)) * (a/(a + d)))/ ((a/(a + b)) + (a/(a + d))))

print('Accuracy: ', accuracy(4, 2, 3, 4),'and F1: ', f1(4, 2, 3, 4))

