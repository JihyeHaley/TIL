import random # 내부 모듈
# pip install requests를 terminal에서 사용하여 requests 모듈을 설치한다!!
import requests # 크롤링하기 위함 !!(내부 모듈 x -> 설치 해야함)

numbers = range(1, 46)
print(list(numbers))
print('-----lotto-----')
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
lotto_info = response.json()
print(lotto_info)

# key값이 조금이라도 틀리면 Error
bonus_num = lotto_info['bnusNo']

# key에 맞는 값이 없다. -> "None"으로 처리된다.
bonus_num = lotto_info.get('bnusNo')
print(bonus_num)

#직접 구현해보기
winner = []


for i in range(1,7) :
    winner.append(lotto_info.get(f'drwtNo{i}'))

print('----lotto number----')
print(winner)
print('----my number----')
print(pick)
    
#나의 결과물
print('----you are..!----')
for i in range(0,5) :
    cnt = 0
    for j in range(0,5) :
        
        if(winner[i]==pick[j]) : 
            cnt = cnt + 1 

if (cnt == 6) :
    print('1등입니다.')
elif (cnt == 5):
    for j in range(1,7) :
        if(pick[j]==bonus_num) :
            print('2등입니다.')
        else :
            print('3등입니다. 아쉽네요. 보너스만 맞춰도 2등인데ㅠㅠ')
elif (cnt == 4) :
        print('4등입니다. 아쉽네요. 보너스만 맞춰도 2등인데ㅠㅠ')
elif (cnt == 3) :
        print('5등입니다. ')
else :
    print('해당사항이 없네요...')    
   

#선생님

set(pick)
set(winner)

match_num = set(pick)& set(winner)
print(len(match_num))