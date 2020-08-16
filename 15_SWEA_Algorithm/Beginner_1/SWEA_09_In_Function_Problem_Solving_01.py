def age():
    name = str(input())
    age = int(input())
    rest = 100 - age  
    print(f'{name}(은)는 {2019 + rest}년에 100세가 될 것입니다.')

age()