# Fibbonacci series
def fibo_series(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else :
        return (fibo_series(n-1)+fibo_series(n-2))
print(fibo_series(10))
# as n becomes larger, the recursive algorithm becomes increasingly inefficient due to the redundant calculations.
