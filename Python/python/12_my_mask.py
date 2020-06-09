import requests
from pprint import pprint

URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
#대문자로 적어주면 "상수"의 느낌을 줄 수 있는 데이터가 된다.

parms = '?address=서울특별시 강남구 역삼동'
response = requests.get(URL+parms)

#print(URL+parms)

#slicing 사용
stores = response.json().get('stores')[:10]

for store in stores:
    #pprint(store)
    store_name = store.get('name')
    remain_mask = store.get('remain_stat')
    
    if remain_mask == 'plenty':
        print(store_name + '\tGreen')
    elif remain_mask == 'some':
         print(store_name + '\tYellow')
    elif remain_mask == 'few':
         print(store_name + '\tRed')
    elif remain_mask == 'break':
         print(store_name + '\tGrey')