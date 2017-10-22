def bombReplication(M, F):
    # your code here
    num = 0
    m = int(M)
    f = int(F)
    if (m == 1 and f == 1):
        return "0"
    elif (m <= 0 or f <= 0 or m == f):
        return "impossible"
    else:
        while (m >= 0 and f >= 0):
            if (f == 0 and m > 0):
                return "impossible"
            elif (m == 0 and f > 0):
                return "impossible"
            elif (m == 1 and f != 1):
                num = num + f - 1
                return str(num)
            elif (m != 1 and f == 1):
                num = num + m - 1
                return str(num)
            elif (m > f):
                num = num + int(m/f)
                m = m % f
            elif (m < f):
                num = num + int(f/m)
                f = f % m
            else:
                return "impossible"
    return str(num)