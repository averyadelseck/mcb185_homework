#Accuracy and F1 Score for Values



def accuracy(tp, fp, tn, fn):

"""tp = true positives, fn = false positives, 
tn = true negatives, fn = false negatives"""
	return(tp + c)/(tp + fp + tn + fn)

def f1(tp, fp, tn, fn):
"""tp = true positives, fn = false positives,
tn = true negatives, fn = false negatives"""
	return((2 * (tp/(tp + fp)) * (tp/(tp + fn)))/ ((tp/(tp + fp)) + (tp/(tp + fn))))

print('Accuracy: ', accuracy(4, 2, 3, 4),'and F1: ', f1(4, 2, 3, 4))

