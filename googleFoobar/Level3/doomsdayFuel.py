from itertools import product 
from fractions import Fraction

## LCM and GCD operations ##
def getGCD(a, b):
    '''Find the GCD of two given numbers'''
    while b:      
        a,b = b,(a % b)
    return a

def getLCM(a):
    '''Find the LCM of a given array of numbers'''
    lcm = a[0]
    n = len(a)
    for i in range(1,n):
        lcm = (a[i]*lcm)//getGCD(a[i],lcm)
    return lcm


## Matrix operations
def invertMatrix(matrix):
    '''Find the inverse of a square matrix'''
    n = len(matrix)
    if n == 1:
        return [1./x for x in matrix]
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False #the matrix is not inversible
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False #the matrix is not inversible
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse
    

def multiplyMatrix(A,B):
    '''Perform the multiplication of two matrices (array of array) and return a array of array as output'''
    rowA = len(A)
    rowB = len(B)
    if not (rowA or rowB):
        return 0
    else:
        colA = len(A[0])
        colB = len(B[0])
    resultRows = range(len(A))
    result = [[0] * colB for row in resultRows]
    for row in resultRows:
        for j, k in product(range(colB), range(rowB)):
            result[row][j] += A[row][k] * B[k][j]
    return result


## Calculate the absorption matrix for absortive Markov chains
def absorptionMatrix(m):
    '''Find the absorption matrix for a given transition probability matrix'''
    size = len(m)
    terminal = [0] * size
    mat = [[0 for x in range(0,size)] for y in range(0,size)]
    rowSum = [0] * size

    for i in range(0,size):
        rowSum[i] = sum(m[i])
        if all(v == 0 for v in [m[i][j] for j in range(0,size) if j != i]):
            terminal[i] = 1
            mat[i][i] = 1
        else:
            terminal[i] = 0
            mat[i] = [x/float(rowSum[i]) for x in m[i]]
   
    order = [] # order list for terminal states
    order1 = [] # order list for non-terminal states
    mat1 = [[0] * size for y in range(0,size)]
    
    for i in range(0,size):
        if terminal[i] == 1:
            order.append(i)
        else:
            order1.append(i)
    order.extend(order1) # combining terminal and non terminal states
    for i,o1 in zip(range(0,size),order):
        for j,o2 in zip(range(0,size),order):
            mat1[i][j] = mat[o1][o2]
    return mat1,terminal

def getFR(absMat,termState):
    '''Find FR from the absorption matrix to get the steady state probabilities'''
    size = len(absMat)
    numTermState = sum(termState)
    rMat = [absMat[numTermState+x][:numTermState] for x in range(0,size-numTermState)]
    qMat = [absMat[numTermState+x][numTermState:] for x in range(0,size-numTermState)]
    iMat = [[1 if x == y else 0 for x in range(0,size-numTermState)] for y in range(0,size-numTermState)]
    IminusQ = [[item1[i] - item2[i] for i in range(0,size-numTermState)] for item1,item2 in zip(iMat,qMat)]
    fMat = invertMatrix(IminusQ)
    fr = multiplyMatrix(fMat,rMat)
    return fr



def doomsdayFuel(m):
    '''Main function to return the steadystate probabilities'''
    size = len(m)
    if size == 0:
        return [0]
    elif size == 1:
        return [1,1]
    else:
        absMat, termState = absorptionMatrix(m)
        fr = getFR(absMat,termState)
        numerator = [Fraction(x).limit_denominator().numerator for x in fr[0]]
        denominator = [Fraction(x).limit_denominator().denominator for x in fr[0]]                              
        lcm = getLCM(denominator)
        factor = [lcm/y for y in denominator]
        prob = [x*f for x,f in zip(numerator,factor)]
        prob.append(lcm)
        return map(int,prob)


#Running some sample test cases

m1 = [[ 0,  7,  0, 17,  0,  1,  0,  5,  0,  2], [ 0,  0, 29,  0, 28,  0,  3,  0, 16,  0], [ 0,  3,  0,  0,  0,  1,  0,  0,  0,  0], [48,  0,  3,  0,  0,  0, 17,  0,  0,  0], [ 0,  6,  0,  0,  0,  1,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
assert doomsdayFuel(m1) == [4, 5, 5, 4, 2, 20]

m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
assert doomsdayFuel(m2) == [0, 3, 2, 9, 14]

m3 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
assert doomsdayFuel(m3) == [3, 4, 7]

m4 = [[0, 0, 12, 0, 15, 0, 0, 0, 1, 8], [0, 0, 60, 0, 0, 7, 13, 0, 0, 0], [0, 15, 0, 8, 7, 0, 0, 1, 9, 0], [23, 0, 0, 0, 0, 1, 0, 0, 0, 0], [37, 35, 0, 0, 0, 0, 3, 21, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
assert doomsdayFuel(m4) == [1, 2, 3, 4, 5, 15]
