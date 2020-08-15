T = int(input())

def fib(T):
    x, y = 0, 1
    fib_gat =[1]
    for i in range(0, T-1):
        x, y = y, x+y
        fib_gat.append(y)
    print(fib_gat)

fib(T)