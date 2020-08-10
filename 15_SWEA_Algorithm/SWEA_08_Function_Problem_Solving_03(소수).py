num = int(input())
divide = []
def check(num):
    for i in range(1, num+1):
        if num % i == 0:
            divide.append(i)

    if len(divide) == 2:
        print('소수입니다.')
check(num)