#Fibonacci fn = fn-1 + fn-2
n=0

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


for i in range (8):
    print(fib(i))
    if n > 2:
        dif = fib(i) / fib(i-1)
        print(dif)
