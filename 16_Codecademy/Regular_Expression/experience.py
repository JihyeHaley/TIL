import re
# str = 'iso |123'
# str2 = 'itt'
# p = re.compile('|')

# if bool(p.match(str2)) == True:
#     print(str2)

# ko_list = 'jihye hi- he_e'
# ko_compare = re.sub(r'_', '', ko_list)
# ko_compare = re.sub(r' ', '', ko_compare)
# ko_compare = re.sub(r'-', '', ko_compare)
# print(ko_compare)


# a = ' | ISOfocus_131'
# b = 'ISOfocus_131 | 11'
# c = ' | ISO포커스_131'
# d = 'ISO포커스_131 | 7'
# tests = list()
# tests.append(a)
# tests.append(b)
# tests.append(c)
# tests.append(d)
# for test in tests:
#     test = re.sub(r"(ISOfocus|ISO포커스)_?\d{1,3}\s*\|\s*\d{1,2}", "", test)
#     test = re.sub(r"\s{1}\|\s{1}(ISOfocus|ISO포커스){1}_{1}\d{1,3}", "", test)
#     print(test)


# a = ' – ISO | 표준 작성 방법'
# b = ' – ISO | How to write standards'
# c= 'jijijji'
# tests = list()
# tests.append(a)
# tests.append(b)
# tests.append(c)
# for test in tests:
#     test = re.sub(r" – ISO \| ", "", test)
#     # test = re.sub(r"\s{1}-\s{1}(ISO)\s{1}\|\s{1}(\w|[ㄱ-ㅣ가-힣])", "", test)
#     print(test)


com1 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-2019 올림피아드 개최 결과 및 2020 개최 계획 (영문)-영.pptx'
com2 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-2019 올림피아드 개최 결과 및 2020 개최 계획 (국문)-한.pptx'
com3 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_259호 (기사 1 + 추가 2)-한.pptx'
com4 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_249호_첨단(기사 1)-영.pptx'
print(com3[:-14])
print(com4[:-14])
com1 = re.sub(r'_', '', com1)
com1 = re.sub(r'-', '', com1)
com1 = re.sub(r'\s{1}', '', com1)
print(com1[:-6])
# /Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_249호_첨단(기사 1)-영.pptx
# /Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_249호 첨단(기사 1)-한.pptx

youtube_url = '/watch?v=RqTZgPuRnpE'

str1 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_259호 (기사 1)-영.pptx'
str2 = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/4.2019한국표준협회/TE-한국표준협회-ISOfocus_259호 (기사 1)-한.pptx'
print(str1[:-5])
print(str2[:-5])

# 파일 이름의 예외로 pair를 못 이룰때를 대비
def check_file_name_exception(file_name):
    file_name = re.sub(r'_', '', file_name)
    file_name = re.sub(r'-', '', file_name)
    file_name = re.sub(r'\s{1}', '', file_name)
    return file_name

if check_file_name_exception(str1)[:-6] == check_file_name_exception(str2)[:-6]:
    print(check_file_name_exception(str1)[:-6])
    print(check_file_name_exception(str2)[:-6])