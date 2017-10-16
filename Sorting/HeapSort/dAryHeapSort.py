# This program implements an D-ary heap data structure
def ParentNode(i,d):
	# i is the given node index and d is the number of child nodes per parent node
	parent = int((i - 1)/d)
	return parent

def ChildNodes(i,d):
	childNodes = [(d*i + j + 1) for j in range(0,d)]
	return childNodes

def Heapify(A,i,size,d):
	childNodes = ChildNodes(i,d)
	heap_size = size
	largest = i
	for chidx in range(0,d):
		node = childNodes[chidx]
		if (node < heap_size):
			if (A[node] > A[largest]):
				largest = node
	if (largest != i):
		A[i],A[largest] = A[largest],A[i]
		Heapify(A,largest,heap_size,d)
	return A

def BuildHeap(A,d):
	heap_size = len(A)
	parent = ParentNode(heap_size - 1,d)
	for i in reversed(xrange(parent + 1)):
		Heapify(A,i,heap_size,d)
	return A

def HeapSort(A,d):
	BuildHeap(A,d)
	heap_size = len(A)
	for i in range(len(A)-1,0,-1):
		A[i],A[0] = A[0],A[i]
		heap_size = heap_size - 1
		Heapify(A,0,heap_size,d)
	return A
