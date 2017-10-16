def selectionsort(A):
    for i in range(len(A)):
        minIdx = i
        for j in range(i+1,len(A)):
            if A[j] < A[minIdx]:
                minIdx = j
        A[i],A[minIdx] = A[minIdx],A[i]
    return A

x = [4,5,2,10,1.2,1.3,1.8,2.1,2.4,2.7,65,3.5,3.9,4.1,4.2,4.3,4.6,4.9,5.3,5.7,6.5,7.2,2.2,1.8]
xSorted = selectionsort(x)
print xSorted