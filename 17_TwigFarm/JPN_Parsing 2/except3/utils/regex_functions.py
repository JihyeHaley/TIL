import re

# 한글 / 영어 둘다 아닌 경우
def neitherKoNorEn(text):
    neither = re.compile('((?![ㄱ-ㅣ가-힣|a-zA-Z]).)*')
    return bool(neither.fullmatch(text))


# 한글이 포함되지 않은 경우
def mustEnglish(text):
    never_ko = re.compile('((?![ㄱ-ㅣ가-힣]).)*')
    return bool(never_ko.fullmatch(text))


# 영어가 포함되어있는 경우
def isEnglish(text):
    en = re.compile('.*[a-zA-Z]+')
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))


# 한글이 포함되어있는 경우
def isKorean(text):
    ko = re.compile('.*[ㄱ-ㅣ가-힣]+')
    # return bool(ko.fullmatch(text))
    return bool(ko.match(text))

