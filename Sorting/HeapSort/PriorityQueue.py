from HeapSort import *

def QInsert(S,key):
	S.append(key)
	heapsize = len(S) #the heapsize increases after the insert
	idx = heapsize - 1
	while idx > 0 :
		parent = ParentNode(idx)
		if S[parent] < S[idx]:
			S[idx], S[parent] = S[parent], S[idx]
		idx = parent
	return S

def QMaximum(S):
	heapsize = len(S)
	maxi = None
	if heapsize > 0:
		maxi = S[0]
	return maxi
		

def QExtractMax(S):
	#this function returns the max element and the new heap after the max element is removed from the set
	heapsize = len(S)
	maxi = None
	if heapsize < 1:
		print "Error: Heap underflow"
		underflow = 1
	else:
		underflow = 0
		maxi = S[0]
		S[0] = S[-1]
		heapsize = heapsize - 1
		if (heapsize > 0):
			Heapify(S,0,heapsize)
		else: S = [] #empty set since heap had only one element
	return S[0:heapsize],maxi,underflow
