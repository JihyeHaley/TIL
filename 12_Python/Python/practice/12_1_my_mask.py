import requests
from pprint import pprint

URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

parms = '?address=서울시 서대문구 신촌동'
response = requests.get(URL+parms)
#print(URL+parms)

#slicing 사용
stores = response.json().get('stores')[:10]