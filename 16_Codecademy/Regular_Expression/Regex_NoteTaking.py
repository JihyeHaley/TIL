import re
print('''
regex 함수를 사용하고 싶으면 'import re'를 해줘야한다.
re.findall()
re.match()
re.search() -> 한 가지밖에 찾아주지 않는다.
re.fullmatch()

## 이건 기본중의 기본!!!!
? -> 0 or 1
+ -> 1 or more
* -> 0 or more
---------------------------------------------------------------------------------
''')

test_case_1 = re.findall('12+', '12 1212 1222') 
print(f'text_case_1: {test_case_1}') # [12, 12, 12, 1222]

test_sample_1 = '1212'

print('test_case_1_match: ', re.match('(12)+', test_sample_1)) # meta
print('test_case_1_search: ', re.search('(12)+', test_sample_1)) # meta
print('test_case_1_findall: ', re.findall('(12)+', test_sample_1)) # 12 
print('test_case_1_fullmatch: ', re.fullmatch('(12)+', test_sample_1).group()) #meta

# 캡쳐
print('''
# 캡쳐
소괄호 ()가 가진 기능은 캡쳐.''')
print(re.findall('A(12)+B', 'A12B'))  # 12
print(re.findall('A(12)+B', 'A1212B')) # 12
print(re.findall('A(12)+B', 'A121212B')) # 12
print(re.findall('A(12)+B', 'A12121212B')) # 12 

print('''안에 있는 소괄호 즉, 캡쳐만 갖고 출력된다.''')
print(re.findall('\d{4}-(\d\d)-(\d\d)', '1996-03-12')) # [('03', '12')]
print(re.findall('\d{4}-(\d\d)-(\d\d)', '1996-03-12 1997-03-21')) # [('03', '12'), ('03', '21')]


print('''____________________________________________
matchObj.groups()
re.search('<regex>', 'comparison')를 통해서 하나의 변수를 만들어 준다. 
.group()   -> 매칭되는 아이를 string으로 출력
.group(n)  -> 매칭되는 아이를 담겨진 순서대로 출력. 0은 full로 나오는거
.groups()  -> 그룹으로 친 소괄호 내용을 tuple로 출력
.start()   -> slicing 시작점
.end()     -> slicing 끝나는점
.span()    -> slicing range
--------------------------------------------''')

matchObj = re.search('match', '\'matchObj\' is a good name, but \'m\' is convenient.')
print('matchObj: ', matchObj)
print('matchObj.group(): ', matchObj.group())
# print('type of matchObj.group(): ', type(matchObj.group()))
print('matchObj.groups(): ', matchObj.groups())
# print('type of matchObj.groups(): ', type(matchObj.groups()))
print('--------------------------------------------')
print('matchObj.start(): ', matchObj.start())
print('matchObj.end(): ', matchObj.end())
print('matchObj.span(): ', matchObj.span())
print('--------------------------------------------')
m = re.search('\d{4}-(\d?\d)-(\d?\d)', '1996-03-12')
print('m: ', m)
print('m.group(): ', m.group()) #string
# print('type!!! m.group(): ', type(m.group())) 
print('m.groups()', m.groups())
print('groups.()는 명시적으로 캡쳐된 아이!! 소괄호로 싸여진 아이을 tuple로 아웃풋 한다.')
print('--------------------------------------------')
print('m.group(0)', m.group(0))
print('m.group(1)', m.group(1))
print('m.group(2)', m.group(2))
print('group의 0 index는 full string, 1 부터는 처음부터 모여진 소괄호 정규식들 string으로 아웃풋')
print('--------------------------------------------')
print('m.groups()', m.groups())
print('잊지마!!!!! groups.()는 명시적으로 캡쳐된 아이!! 소괄호로 싸여진 아이을 tuple로 아웃풋 한다.')
print('---------------------캡쳐-----------------------')
matchObj = re.search('((ab)+), ((123)+) is repetitive\.', 'Hmm... ababab, 123123 is repetitive.')
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))
print(matchObj.group(3))
print(matchObj.group(4))
print('---------------------비캡쳐-----------------------')
print('using.... (?:<regex>)')
matchObj = re.search('((?:ab)+), ((?:123)+) is repetitive\.', 'Hmm... ababab, 123123 is repetitive.')
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))

