




def fib(n):
    if n <=2 : return 1
    i = 3
    a , b = 1, 1
    while i <= n:
        a , b = a + b, a
        i += 1
    return a

        