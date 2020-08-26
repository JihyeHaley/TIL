def Capital():
    result1 = []
    result2 = []
    T = int(input())
    for i in range(0, T):
        case = list(map(str, input().split()))
        for j in range(0, len(case)):
            first = case[j].capitalize()
            if j == 0:
                result1 = first[0]
            else:
                result1 += first[0]
            result2.append(result1)
    
    for k in range(0, T):
        print(f'#{k+1} {result2[k]}')
Capital() 