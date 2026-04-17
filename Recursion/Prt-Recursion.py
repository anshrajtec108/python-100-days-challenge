# print the N - 1 nuber using Recursion 

def funPrintNum(n):
    if n<1:
        return
    print(n)
    funPrintNum(n-1)

n=100
funPrintNum(n)