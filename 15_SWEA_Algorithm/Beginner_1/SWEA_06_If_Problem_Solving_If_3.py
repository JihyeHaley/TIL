T = str(input())

string = '%c' %(T)
# c: %c (문자포맷, 정수를 유니코드로)

if ord(string) >= 97 & ord(string) <=122:
    print('{0} 는 소문자 입니다.' .format(string))