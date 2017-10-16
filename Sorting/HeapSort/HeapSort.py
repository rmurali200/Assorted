def ParentNode(l):
	parent = int((l - 1)/2.0)
	return parent

def childNodes(i):
	leftNode = 2*i + 1
	rightNode = 2*i + 2
	return leftNode,rightNode

def Heapify(A,i,size):
	left, right = childNodes(i)
	heap_size = size
	if (left < heap_size):
		if (A[left] > A[i]):
			largest = left
		else:
			largest = i
	else: return A
	if (right < heap_size):
		if (A[right] > A[largest])
			largest = right
	if (largest != i):
		A[i],A[largest] = A[largest],A[i]
		Heapify(A,largest,heap_size)
	return A

def BuildHeap(A):
	heap_size = len(A)
	parent = ParentNode(heapsize-1)
	for i in reversed(xrange(parent + 1)):
		Heapify(A,i,heap_size)
	return A

def HeapSort(A):
	BuildHeap(A)
	heap_size = len(A)
	for i in range(len(A)-1,0,-1):
		A[i],A[0] = A[0],A[i]
		heap_size = heap_size - 1
		Heapify(A,0,heap_size)
	return A
