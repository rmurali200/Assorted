def powerHungry(xs):
    # your code here
    prod,prodNeg = 1,1
    zero = [xs.index(x) for x in xs if x == 0]
    pos = [x for x in xs if x > 0]
    prod = reduce(lambda x,y : x * y, pos, 1)
    neg = [y for y in xs if y < 0]
    if (not pos and not neg):
        return str(0)
    if (not pos and len(neg) == 1):
        if zero:
            return str(0)
        else:
            return str(neg[0])
    if len(neg) > 1:
        if ((len(neg) % 2) != 0):
            neg.remove(max(neg))
        prodNeg = reduce(lambda x,y : x * y, neg, 1)        
    return str(prod*prodNeg)