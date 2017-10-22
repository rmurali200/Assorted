def fuelInjection(n):
    n_binary = 0
    n = int(n)
    if (n == 0 or n == 1):
        return 0
    elif n == 2:
        return 1
    elif (n == 3 or n == 4):
        return 2
    else:
        if (n % 2 == 0):
            n_binary = 1 + fuelInjection(n >> 1)
        elif (n % 4 == 1):
            n_binary = 2 + fuelInjection((n-1) >> 1)
        else:
            n_binary = 2 + fuelInjection((n+1) >> 1)
    return n_binary