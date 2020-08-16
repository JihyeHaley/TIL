data_list = list(range(1, 21))
map_list = []
filter_list = []

# map 적용
map_list = list(map(lambda x: x + 3, data_list))

# filter 적용
filter_list = list(filter(lambda x: x % 5==0, data_list))

print(f'map 함수의 적용 결과: {map_list}\nfilter 함수의 적용 결과: {filter_list}')
