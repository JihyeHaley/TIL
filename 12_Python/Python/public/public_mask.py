import requests
from pprint import pprint

# 인자뒤에 =m 하면 default값을 주는 설정 하는 것
def mask(address, n=10):
    parms = f'?address={address}'
    URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
        
    response = requests.get(URL+parms)
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