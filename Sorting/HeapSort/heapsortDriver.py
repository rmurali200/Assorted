from dAryHeapSort import *
from dAryPriorityQueue import *

A = [1900,1,3,5,8,0,22,3,45,32,78,82,100,19,23,4,10,12,200,-1,2000,2100]
d = 2
#A = [1,12,3,4,15,6,7,8]
BuildHeap(A,d)
print A
HeapSort(A,d)
print A
print "Reset A to original array"
A = [1900,1,3,5,8,0,22,3,45,32,78,82,100,19,23,4,10,12,200,-1,2000,2100]
print "Inserting 101 to the heap"
QInsert(A,101,d)
print A
print "Finding the max"
print QMaximum(A,d)
print "Extracting the max"
A, maxi, underflow = QExtractMax(A,d)
print "Max: ", maxi, "underflow: ", underflow
print A
print HeapSort(A,d)
