T = int(input())
maxi = []
mini = []

for i in range(0, T):
    N, P, T = input().split()
    N = int(N)
    P = int(P)
    T = int(T)
    maximum = 0
    minimum = 0
    if N < P+T:
        if P > T:
            maximum = T
            minimum = P-T
        elif T > P:
            maximum = P
            minimum = T-P
        elif T == P:
            maximum = P
            minimum = P 
        
    elif N > P + T:
        minimum = 0
        if P < T:
            maximum = T
        if T < P:
            maximum = P
        
    maxi.append(maximum)
    mini.append(minimum)

for i in range(0, T):
    print(f'#{i+1} {maxi[i]} {mini[i]}')