def Sum_of_first_N_numbers(n):
    if n==0:
        return 0
    return n+Sum_of_first_N_numbers(n-1)

n=4
print(Sum_of_first_N_numbers(n))