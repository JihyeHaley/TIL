import random

import requests

numbers = range(1,46)
print(list(numbers))
print('----lotto----')
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
lotto_info = response.json()

# kye값으로 바로 접근하면 인자 스펠링 하나라도 틀리면 error발생
print('----kye값으로 바로 접근하면 인자 스펠링 하나라도 틀리면 error발생----')
totalamount = lotto_info['totSellamnt']
print(totalamount)
print('----get()으로 접근해야지 null 값일때 error 안나고 \'none\'으로 출력----')
totalamount_error = lotto_info.get('totSellmnt')
print(totalamount_error)
totalamount_2 = lotto_info.get('totSellamnt')
print(totalamount_2)

winner = []

for i in range(1, 7):
    winner.append(lotto_info.get(f'drwtNo{i}'))

print('----lotto number----')
print(winner)
print('----my number----')
pick2 = random.sample(numbers, 6)
print(pick2)


#bonus 
bonus_num = lotto_info.get('bnusNo')

# my result
print('----mine is...----')
for i in range(0, 5):
    cnt = 0
    for j in range(0, 5):
        if winner[i] == pick2[j]:
            cnt = cnt + 1

if cnt == 6:
    print('1등입니다.')
elif cnt ==5:
    for j in range(1, 7):
        if(pick[j] == bonus_num):
            print('2등입니다.')
        else:
            print('3등입니다. bonus못 맞췄네요.')
elif cnt ==4:
    print('4등입니다.')
elif cnt ==3:
    print('5등입니다.')
else:
    print('해당사항이 없습니다.')

print(dir(set))

match_num = set(pick)&set(winner)
print(len(match_num))