#Accuracy and F1 Score for Values

'''
doc-strings:
a = true positives 1
b = false positives 2
c = true negatives 3
d = false negatives 4
'''

def accuracy(tp, fp, tn, fn):
	return(tp + c)/(tp + fp + tn + fn)

def f1(tp, fp, tn, fn):
	return((2 * (tp/(tp + fp)) * (tp/(tp + fn)))/ ((tp/(tp + fp)) + (tp/(tp + fn))))

print('Accuracy: ', accuracy(4, 2, 3, 4),'and F1: ', f1(4, 2, 3, 4))

