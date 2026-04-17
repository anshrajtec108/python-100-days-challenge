
def factorialOfN(n):

    if n == 0:
        return 1
    return n*factorialOfN(n-1)


print(factorialOfN(4))