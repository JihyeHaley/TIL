T = int(input())

divide = []

def division(T):
    for i in range(1, T+1):
        if T%i == 0:
            divide.append(i)

    for j in range(0, len(divide)):
        print('{0}(은)는 {1}의 약수입니다.' .format(divide[j], T))

    if len(divide) == 2:
        print('{0}(은)는 {1}과 {2}로만 나눌 수 있는 소수입니다.' .format(T, divide[0], divide[1]))

division(T)