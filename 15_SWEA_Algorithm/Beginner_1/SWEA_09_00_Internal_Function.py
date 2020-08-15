# API (Application Programming Interface)
# 내장함수!
#   수치형 데이터 조작을 위한 함수
#   집합과 원소 사이의 관계를 다루는 함수
#   각종 변환 함수

# 수칙연산 
# 절대값 // abs()
# 나머지 몫 // divmod()
# 제곱 // pow()
val1, val2 = 9, 5
result_tuple = divmod(val1, val2)

print('divmod({0}, {1}) => 몫: {2} 나머지:{3}' .format(val1, val2, *result_tuple))

data_list = [1, 2, 3, 4, 5]

print('pow({0}, 2) => {1}' .format(data_list[2], pow(data_list[2], 2)))

print('list(map(lambda x: pow(x, 2), {0})) => {1}' .format(data_list, list(map(lambda x: pow(x, 2), data_list))))