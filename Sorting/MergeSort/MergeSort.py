def MergeSort(A):
    n = len(A)
    m = int(n/2)
    Adash = list()
    if n == 1:
        return A
    elif n != 0:
        B = MergeSort(A[0:m]) #remember the last element is not included in the sliced array
        C = MergeSort(A[m:n])
        Adash = Merge(B,C)
    return Adash

def Merge(B,C):
    D = list()
    while len(B) != 0 and len(C) != 0:
        if B[0] <= C[0]:
            D.append(B.pop(0))
        else:
            D.append(C.pop(0))
    D = D + B + C
    return D

def SelectionSort(A):
    for i in range(len(A)):
        minIdx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIdx]:
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]
    return A

x = [4,3,5,2,10,1.2,1.3,1.8,2.1,2.4,2.7,3.5,65,3.9,4.1,4.2,4.3,4.6,4.9,5.3,5.7,6.5,7.2,2.2,1.8,1]
xSorted = MergeSort(x)
print xSorted
xSorted1 = SelectionSort(x)
print xSorted1
if xSorted == xSorted1:
    print "The two methods produce same results"

