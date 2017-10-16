def QuickSort(A,l,r):
    if l >= r:
        return
    m = Partition(A,l,r)
    QuickSort(A,l,m-1)
    QuickSort(A,m+1,r)
    return A

def Partition(A,l,r):
    pivot = A[l]
    j = l
    for i in range(l+1,r+1):
        if A[i] <= pivot:
            j = j+1
            A[i],A[j] = A[j],A[i]
    A[l],A[j] = A[j],A[l]
    return j

x = [45,2,10,11.3,21.8,12.1,42.4,32.7,23.5,465,13.9,14.1,4.2,4.3,74.6,34.9,25.3,51.7,69.5,17.2,22.2,21.8,31,65]
xSorted = QuickSort(x,0,len(x)-1)
print xSorted
print len(x),len(xSorted)
