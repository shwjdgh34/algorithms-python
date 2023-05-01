def fibo(n):
    if n == 1 or 2: 
        return 1
    return fibo(n-1) + fibo(n-2)