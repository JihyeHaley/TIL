F = int(input())

def fac(F):
    result = 1
    for i in range(1, F+1):
        result = result*i
    print(result)

fac(F)