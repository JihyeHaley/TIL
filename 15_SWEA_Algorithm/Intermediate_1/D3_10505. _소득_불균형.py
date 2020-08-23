print('''
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.

첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다. 이 정수들은 각각 1 이상 100,000 이하이다.
 

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.
''')


T = int(input())
total_gdp = 0
avg_adp = 0
case = []
cnt = 0
result = []

def AvGDP():
    total_gdp = 0
    avg_gdp = 0
    # 인원 수
    N = int(input())
    case = [int(x) for x in input().strip().split()]
    total_gdp = sum(case)
    avg_gdp = total_gdp // N 
    cnt = list(filter(lambda x: x <= avg_gdp, case))
    result.append(len(cnt))

for i in range(0, T):
    AvGDP()

for j in range(0, T):
    print(f'#{j+1} {result[j]}') 
