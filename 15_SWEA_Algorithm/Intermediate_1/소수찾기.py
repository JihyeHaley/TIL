def onlyNum():
    num = int(input('input an int: '))
    # cnt = 0
    result = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            result.append(i)
    print(result)
    if len(result) == 2:
        print(f'{result}의 개수가 {len(result)}개이므로 소수입니다.')
    else:
        print(f'{result}의 개수가 {len(result)}개이므로 소수가 아닙미다.')

onlyNum()
