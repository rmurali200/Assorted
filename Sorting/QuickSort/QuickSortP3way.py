import random

def QuickSortP3Way(A,l,r):
    if l >= r:
        return
    k = random.randint(l,r)
    A[k],A[l] = A[l],A[k]
    (m1,m2) = Partition3Way(A,l,r)
    QuickSortP3Way(A,l,m1-1)
    QuickSortP3Way(A,m2+1,r)
    return A

def Partition3Way(A,l,r):
    pivot = A[l]
    j,k = l,l
    for i in range(l+1,r+1):
        if A[i] < pivot:
            j = j+1
            A[i],A[j] = A[j],A[i]
        elif A[i] == pivot:
            k = j+1
    A[l],A[j] = A[j],A[l]
    return j,k

x = [45,2,10,11.3,21.8,12.1,42.4,32.7,23.5,465,13.9,10,10,10,10,10,10,10,190,14.1,4.2,4.3,74.6,34.9,25.3,51.7,69.5,17.2,22.2,21.8,31,65]
xSorted = QuickSortP3Way(x,0,len(x)-1)
print xSorted
print len(x),len(xSorted)