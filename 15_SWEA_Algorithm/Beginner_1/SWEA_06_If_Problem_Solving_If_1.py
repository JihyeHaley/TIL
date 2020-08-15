T = int(input())

divide = []

def division(T):
    for i in range(1, T+1):
        if T%i == 0:
            divide.append(i)

    for j in range(0, len(divide)):
        print('{0}(은)는 {1}의 약수입니다.' .format(divide[j], T))

division(T)